import telebot, requests, json,logging
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
API = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={0}&tsyms={1}'

def getPrice(DIGITAL_CURRENCY, CURRENCY):
	URL = API.format(DIGITAL_CURRENCY, CURRENCY)
	response = requests.get(URL)
	out = json.loads(response.content)
	BTC = out[DIGITAL_CURRENCY]
	USD = BTC[CURRENCY]
	return USD*6.31

#bot.send_message("@testmypythonbot", text = DIGITAL_CURRENCY + ' Price :' + str(getPrice('BTC', 'USD')))
bot.send_message("@testmypythonbot", text = 'ETH' + ' Price :' + str(getPrice('ETH', 'USD')))
bot.send_message("@testmypythonbot", text = 'BCC' + ' Price :' + str(getPrice('BCC', 'USD')))
