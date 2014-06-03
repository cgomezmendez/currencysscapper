from lxml import html
import requests
import re

class Scrapper:
	# this method returns a diccionary with dollar and euro exchange
	# rate of current day
	@staticmethod
	def getCurrencies():
		currencies  = {};
		response = requests.get('http://www.elcaribe.com.do/')
		parse = html.fromstring(response.text)
		currenciesSpan = parse.xpath('//div[@class="dolar"]//span')
		dollarStr = currenciesSpan[0].text;\
		currencies['dollar'] = re.findall('\d+\.\d+',dollarStr)[0]
		euroStr = currenciesSpan[1].text
		currencies['euro'] = re.findall('\d+\.\d+',euroStr)[0]
		return currencies