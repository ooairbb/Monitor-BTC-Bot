import telebot, requests, json, logging
from requests.packages import urllib3
from config import TOKEN

urllib3.disable_warnings()
bot = telebot.TeleBot(TOKEN)
API = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={0}&tsyms={1}'
DIGITAL_CURRENCY_LIST = ['BTC','ETH']
CURRENCY_LIST = ['USD','CNY']


def getprice(DIGITAL_CURRENCY_LIST, CURRENCY_LIST):
	digital_currency_list = ','.join(DIGITAL_CURRENCY_LIST) #List Covert To String By ','
	currency_list = ','.join(CURRENCY_LIST)
	print digital_currency_list
	print currency_list

	URL = API.format(digital_currency_list, currency_list)
	response = requests.get(URL, verify=False).json()
	if response is not None:
		return response
	else:
		return 'ERROR'

def sendtoot(info, DIGITAL_CURRENCY_LIST, CURRENCY_LIST):
	result = ''
	for i in DIGITAL_CURRENCY_LIST:
		for x in CURRENCY_LIST:
			temp = info[i]
			print temp[x]
			result += i + ' ' + x + str(temp[x]) + '|'
	bot.send_message("@testmypythonbot", text = result)
sendtoot(getprice(DIGITAL_CURRENCY_LIST, CURRENCY_LIST), DIGITAL_CURRENCY_LIST, CURRENCY_LIST)
#bot.send_message("@testmypythonbot", text = DIGITAL_CURRENCY + ' Price :' + str(getPrice('BTC', 'USD')))
#bot.send_message("@testmypythonbot", text = 'ETH' + ' Price :' + str(getPrice('ETH', 'USD')))
#bot.send_message("@testmypythonbot", text = 'BCC' + ' Price :' + str(getPrice('BCC', 'USD')))
