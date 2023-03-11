from DataBase import DB_Commands
import BotVk
import json


DB_Commands.createUserDB()

BotVk.startBot()
"""
try:
    DB_Commands.create_new_user(3)
except DB_Commands.sqlite3.IntegrityError:
    print("daad")
except Exception as s:
    print(f"Unexpected {s=}, {type(s)=}")
"""