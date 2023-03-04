import sys
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import datetime
import BotVk
import menu_templates
from DataBase import DB_Commands


def sendMsg(data):
    if data["keyboard"] != None:
        data["keyboard"] = data["keyboard"].get_keyboard()
    BotVk.vk.messages.send(
        random_id=get_random_id(),
        peer_id=data["peer_id"],
        message=data["message"],
        attachment=data["attachment"],
        keyboard=data["keyboard"]
    )


def create_Person(request):
    try:
        DB_Commands.addNewUser(request["from_id"])
        data = {
            "peer_id": request["peer_id"],
            "message": f"@id{request['from_id']}, теперь у вас есть персонаж! Постарайся не попасть в рабство..."
        }
        sendMsg(data)
    except Exception:
        pass


def about_Person(event):
    data = menu_templates.aboutMenu(
        fromId=event.obj["message"]["from_id"],
        peerId=event.obj["message"]["peer_id"],
        fromUser=event.from_user
    )
    sendMsg(data)


def handler(event):
    text = event.obj["message"]["text"].lower()

    try:
        DB_Commands.addNewUser(event.obj["message"]["from_id"])


    except DB_Commands.sqlite3.IntegrityError:
        if text == "обо мне":
            about_Person(event)


    except Exception as s:
        print(f"Unexpected {s}\n{s=}, {type(s)=}")
