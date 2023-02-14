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
        DB_Commands.add_new_user(request["from_id"])
        data = {
            "peer_id": request["peer_id"],
            "message": f"@id{request['from_id']}, теперь у вас есть персонаж! Постарайся не попасть в рабство..."
        }
        sendMsg(data)
    except Exception:
        pass


def about_Person(event):
    data = menu_templates.about_Person(
        from_id=event.obj["message"]["from_id"],
        peer_id=event.obj["message"]["peer_id"],
        from_user=event.from_user
    )
    sendMsg(data)


def handler(event):
    text = event.obj["message"]["text"].lower()

    if text == "обо мне":
        about_Person(event)
    else:
        create_Person(event)
