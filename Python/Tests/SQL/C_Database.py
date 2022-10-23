import sqlite3

def initDB(name):
    '''
    A function to create a database using sqlite3. Variable 'name' is a string to name the new database
    :param name:
    :return name:
    '''
    try:
        name = str(name)
    except ValueError:
        print('The name input is not a string and cannot be made into one')
    try:

        connection = sqlite3.connect(name)

        con_cursor = connection.cursor()

        connection.close()
    except sqlite3.Error as error:
        print("Failed to create database", error)


def makeTable(dbName,tableName):
    try:
        dbName = str(dbName)
    except ValueError:
        print('The name of the database you put in is not a string, nor compatible with one')

    try:
        tableName = str(tableName)
    except ValueError:
        print('The name for a new table that you input is not a string, nor compatible with one')

    try:
        con = sqlite3.connect(dbName)
        con_cursor = con.cursor()
        sql_command = """CREATE TABLE IF NOT EXISTS tableName (pName, pLevel, pGuesses)"""
        con_cursor.execute(sql_command)

        con.close()
    except sqlite3.error as error:
        print("failed to create table",error)

def data_entry(dbName,tableName, playerName):

