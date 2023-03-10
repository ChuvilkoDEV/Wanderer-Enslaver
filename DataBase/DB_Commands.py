import sqlite3
import json
import datetime

connect = sqlite3.connect('DataBase/users.db')

def strToDatetime(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')


def DatetimeToStr(time:datetime):
    return time.strftime('%Y-%m-%d %H:%M:%S')

# Создает базу данных, если она не была создана ранее
def createUserDB():
    cursor = connect.cursor()

    with open('DataBase/db_config.txt', 'r', encoding="utf-8") as f:
        cursor.execute(f.read())
        connect.commit()

def generateInsertString(nParameters):
    string = 'INSERT INTO users VALUES(?'
    for i in range(nParameters - 1):
        string += ',?'
    string += ')'
    return string

def dictToList(data:dict):
    res = []
    for i in data:
        res.append(data[i])
    return res

def addNewUser(userId):
    cursor = connect.cursor()
    cursor.execute(f'INSERT INTO users (user_id) VALUES ({userId})')
    connect.commit()

# Возвращает настройки пользователя user_id
def selectAllSettingsUserDB(userId):
    cursor = connect.cursor()
    data = cursor.execute('SELECT * FROM users WHERE user_id == ?', (userId,)).fetchone()
    return data

# Возвращает поля введенные в конфиг, по адресу wayToConfig для пользователя под индексом userId
def selectSettingsByConfig(config, userId:int):
    if (config["getFromDB"] != ""):
        cursor = connect.cursor()
        data = cursor.execute(config["getFromDB"], (userId,)).fetchone()
        index = 0
        for i in config["data"]:
            config["data"][i] = data[index]
            index += 1
        return config


def insertSettingsByConfig(insertString:str, data:list, userId:int):
    if (insertString != ""):
        cursor = connect.cursor()
        data.append(userId)
        cursor.execute(insertString, data)
        connect.commit()

