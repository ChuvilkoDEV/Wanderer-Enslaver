from DataBase import DB_Commands
import BotVk

DB_Commands.create_user_db()

BotVk.startBot()

"""
try:
    DB_Commands.create_new_user(3)
except DB_Commands.sqlite3.IntegrityError:
    print("daad")
except Exception as s:
    print(f"Unexpected {s=}, {type(s)=}")
"""