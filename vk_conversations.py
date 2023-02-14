import sys
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import datetime
import BotVk
from DataBase import DB_Commands
from buttons import *


def replaceFString(s, data):
    for i in range(len(data)):
        if s.find(f"<<{i}>>"):
            s = s.replace(f"<<{i}>>", str(data[i]))
    return s


def create_Person(request):
    try:
        DB_Commands.add_new_user(request["from_id"])
        BotVk.Write_conversationMessages(BotVk.vk, request["peer_id"],
                                         f"@id{request['from_id']}, теперь у вас есть персонаж! Постарайся не попасть в рабство...")
    except Exception:
        pass


def about_Person(request):
    try:
        buttons = (slavesBtn, skillsBtn, None, inventoryBtn, equipmentBtn, None, jobBtn)
        keyboard = VkKeyboard(inline=True)
        keyboard = addButtons(keyboard, buttons)

        data = DB_Commands.select_AboutSettings_user_db(request["from_id"])
        with open('DataBase/text/about_text.txt', 'r', encoding="utf-8") as f:
            BotVk.Write_conversationMessages(BotVk.vk, request["peer_id"], replaceFString(f.read(), data),
                                             keyboard=keyboard)

    except Exception as s:
        print(f"Unexpected: {s}\n{s=}, {type(s)=}")


def conversation(event):
    request = event.obj["message"]
    text = request["text"].lower()
    now = datetime.datetime.now()

    if text == "обо мне":
        about_Person(request)
    else:
        create_Person(request)
