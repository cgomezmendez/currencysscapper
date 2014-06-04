from datetime import date
from pony.orm import *
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')
database = config.get('database','database')
host = config.get('database','host')
username = config.get('database','username')
password = config.get('database','password')
databaseName = config.get('database','database_name')

db = Database(database, host=host, user=username,
 passwd=password, db=databaseName)

class Currency(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    currencyvalues = Set("CurrencyValue")

class CurrencyValue(db.Entity):
    id = PrimaryKey(int, auto=True)
    currency = Required(Currency)
    date = Required(date, unique=False)
    value = Required(float)
sql_debug(True)
db.generate_mapping(create_tables=True)

@db_session
def createCurrencies():
	if (Currency.get(name="dollar") is None):
		dollar = Currency(name="Dollar")
	if (Currency.get(name="euro") is None):
		euro = Currency(name = "Euro")