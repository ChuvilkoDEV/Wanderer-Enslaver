import sqlite3
import json
import datetime

defaultUser = []
with open('DataBase/defaultUser.json', 'r', encoding='utf-8') as f: #открываем файл на чтение
    tmp = json.load(f)
    for i in tmp:
        defaultUser.append(str(tmp[i]))

# Создает базу данных, если она не была создана ранее
def create_user_db():
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()

    with open('DataBase/db_config.txt', 'r') as f:
        cursor.execute(f.read())
        connect.commit()

def generate_insert_string(n_parameters):
    string = 'INSERT INTO users VALUES(?'
    for i in range(n_parameters - 1):
        string += ',?'
    string += ')'
    return string

def add_new_user(user_id):
    data = [user_id]
    data += defaultUser
    data.append(datetime.datetime.now())
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    cursor.execute(generate_insert_string(len(data)), data)
    connect.commit()

# Возвращает настройки пользователя user_id
def select_AllSettings_user_db(user_id):
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    data = cursor.execute('SELECT * FROM users WHERE user_id == ?', (user_id,) ).fetchone()
    return data

# Возвращает поля введенные в конфиг, по адресу wayToConfig для пользователя под индексом user_id
def select_settings_byConfig(config:str, user_id:int):
    if (config == ""):
        return
    connect = sqlite3.connect('DataBase/users.db')
    cursor = connect.cursor()
    return cursor.execute(config, (user_id,) ).fetchone()

