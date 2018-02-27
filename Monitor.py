import telebot, requests, json,logging
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
URL_BTC = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD'

def getprice():
	response = requests.get(URL_BTC)
	out = json.loads(response.content)
	BTC = out['BTC']
	USD = BTC['USD']
	return USD*6.31

bot.send_message("@testmypythonbot", text = 'BTC Price :' + str(getprice()))
