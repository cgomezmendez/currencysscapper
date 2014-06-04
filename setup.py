#!/usr/bin/env python
import ConfigParser

def writeConfig(dbms,host,username,password,name):
	config = ConfigParser.RawConfigParser()
	config.add_section('database')
	config.set('database','database',dbms)
	config.set('database','host',host)
	config.set('database','username',username)
	config.set('database','password',password)
	config.set('database','database_name',name)
	with open('config.cfg','wb') as configfile:
			config.write(configfile)

def inputDbms():
	dbmsSelection = raw_input('''
Selecte your DBMS:\n 
	1) mysql
	2) sqlite
	3) postgresql
	4) oracle
''')
	if dbmsSelection.isdigit():
		dbmsSelection = int(dbmsSelection)
	return dbmsSelection

dbmsDiccionary = {1 : 'mysql',2 : 'sqlite',
3: 'postgres', 4 : 'oracle'}
dbmsSelection = 0;
while True:
	dbmsSelection = inputDbms()
	if dbmsSelection in dbmsDiccionary:
		break
dbms = dbmsDiccionary[dbmsSelection];
host = raw_input('Enter your database host (localhost):')
if not host:
	host = 'localhost'
username = raw_input('''
Enter your database username:
''')
password = raw_input('''
Enter your database password:
''')
name = raw_input('''
Enter your database name (currenciesdb):
''')
if not name:
	name = 'currenciesdb'
writeConfig(dbms,host,username,password,name)

