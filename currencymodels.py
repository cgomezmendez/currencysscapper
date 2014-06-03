from datetime import date
from pony.orm import *

db = Database("mysql", host="localhost", user="root", passwd="elcj2304", db="currenciesdb")

class Currency(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    currencyvalues = Set("CurrencyValue")

class CurrencyValue(db.Entity):
    id = PrimaryKey(int, auto=True)
    currency = Required(Currency)
    date = Required(date, unique=True)
    value = Required(float)

db.generate_mapping(create_tables=True)

@db_session
def createCurrencies():
	if (Currency.get(name="dollar") is None):
		dollar = Currency(name="Dollar")
	if (Currency.get(name="euro") is None):
		euro = Currency(name = "Euro")