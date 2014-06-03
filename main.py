#!/usr/bin/env python
from currencyscrapper import Scrapper
from currencymodels import *
import time

@db_session
def saveCurrenciesTodayData():
	currenciesTodayValues = Scrapper.getCurrencies()
	currentDate = time.strftime("%d/%m/%Y")
	currencies = Scrapper.getCurrencies();
	currentDollarValue = CurrencyValue.get(date=currentDate)
	if (currentDollarValue is None):
		currentDollarValue  = CurrencyValue(date=currentDate,currency=Currency.get(name="Dollar"),value=currencies['dollar'])
	else:
		currentDollarValue.value = currencies['dollar']
	currentEuroValue = CurrencyValue.get(date=currentDate)
	if (currentEuroValue is None):
		currentEuroValue  = CurrencyValue(date=currentDate,currency=Currency.get(name="Euro"),value=currencies['euro'])
	else:
		currentEuroValue.value = currencies['euro']

createCurrencies()
saveCurrenciesTodayData()