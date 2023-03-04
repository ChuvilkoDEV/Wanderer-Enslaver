from DataBase import DB_Commands
import BotVk
import json
import DataBase.defaultUser


DB_Commands.create_user_db()
DataBase.defaultUser.generateDefaultUser()

BotVk.startBot()
"""
try:
    DB_Commands.create_new_user(3)
except DB_Commands.sqlite3.IntegrityError:
    print("daad")
except Exception as s:
    print(f"Unexpected {s=}, {type(s)=}")
"""