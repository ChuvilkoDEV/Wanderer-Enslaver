import sqlite3
import json
import datetime

defaultUser = []
with open('DataBase/defaultUser.json', 'r', encoding='utf-8') as f: #открываем файл на чтение
    tmp = json.load(f)
    for i in tmp:
        defaultUser.append(str(tmp[i]))

# Создает базу данных, если она не была создана ранее
def createUserDB():
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()

    with open('DataBase/db_config.txt', 'r') as f:
        cursor.execute(f.read())
        connect.commit()

def generateInsertString(nParameters):
    string = 'INSERT INTO users VALUES(?'
    for i in range(nParameters - 1):
        string += ',?'
    string += ')'
    return string

def addNewUser(userId):
    data = [userId]
    data += defaultUser
    data.append(datetime.datetime.now())
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    cursor.execute(generateInsertString(len(data)), data)
    connect.commit()

# Возвращает настройки пользователя user_id
def selectAllSettingsUserDB(userId):
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    data = cursor.execute('SELECT * FROM users WHERE user_id == ?', (userId,)).fetchone()
    return data

# Возвращает поля введенные в конфиг, по адресу wayToConfig для пользователя под индексом user_id
def selectSettingsByConfig(config:str, userId:int):
    if (config == ""):
        return
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    return cursor.execute(config, (userId,)).fetchone()

