import sqlite3

conn = sqlite3.connect('number_gameDB')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS scores (pName TEXT, pLevel, pGuess')

def data_entry():
    c.execute()