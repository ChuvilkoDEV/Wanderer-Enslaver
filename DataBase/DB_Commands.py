import sqlite3
import json
import datetime

defaultUser = []
with open('DataBase/defaultUser.json', 'r', encoding='utf-8') as f: #открываем файл на чтение
    tmp = json.load(f)
    for i in tmp:
        defaultUser.append(str(tmp[i]))

def strToDatetime(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')


def DatetimeToStr(time:datetime):
    return time.strftime('%Y-%m-%d %H:%M:%S')

# Создает базу данных, если она не была создана ранее
def createUserDB():
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()

    with open('DataBase/db_config.txt', 'r', encoding="utf-8") as f:
        cursor.execute(f.read())
        connect.commit()
        cursor.close()

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
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    cursor.execute(f'INSERT INTO users (user_id) VALUES ({userId})')
    connect.commit()
    cursor.close()
    connect.close()

# Возвращает настройки пользователя user_id
def selectAllSettingsUserDB(userId):
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    data = cursor.execute('SELECT * FROM users WHERE user_id == ?', (userId,)).fetchone()
    cursor.close()
    connect.close()
    return data

# Возвращает поля введенные в конфиг, по адресу wayToConfig для пользователя под индексом user_id
def selectSettingsByConfig(config, userId:int):
    if (config["getFromDB"] != ""):
        connect = sqlite3.connect('DataBase/users.db')
        cursor = connect.cursor()
        data = cursor.execute(config["getFromDB"], (userId,)).fetchone()
        cursor.close()
        connect.close()
        index = 0
        for i in config["data"]:
            config["data"][i] = data[index]
            index += 1
        return config

# Возвращает поля введенные в конфиг, по адресу wayToConfig для пользователя под индексом user_id
def insertSettingsByConfig(insertString:str, data:list, userId:int):
    if (insertString != ""):
        connect = sqlite3.connect('DataBase/users.db')
        cursor = connect.cursor()
        data.append(userId)
        cursor.execute(insertString, data)
        connect.commit()
        cursor.close()
        connect.close()

