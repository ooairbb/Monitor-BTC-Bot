from bs4 import BeautifulSoup
import telebot, requests, json,logging, os
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

JIANDAN_URL = 'http://jandan.net/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}

def getFirstPage(url, headers):
	urllist = readFile('urllist.txt')
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.text,'lxml')
	all = soup.find_all('h2')
	for i in all:
		url = i.a['href']
		print i.a.get_text() #url_contents
		if url not in urllist:
			urllist.append(url)
			saveList(url)
	#result = json.dumps(urllist, encoding = 'utf-8', ensure_ascii=False)
			bot.send_message("@testmypythonbot", text = url)
	return urllist
	

def saveList(url):
	with open('urllist.txt','a+') as f:
		f.write(url + '\n')

def readFile(filename):
	list = []
	if not(os.path.exists(filename) and os.path.isfile(filename)):
		os.mknod(filename)
	else:
		with open(filename, 'r') as f:
			for line in f:
				list.append(line.rstrip())
	return list

print getFirstPage(JIANDAN_URL, HEADERS)

#readFile('urllist.txt')
#saveList(getFirstPage(JIANDAN_URL, HEADERS))
