import time

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from threading import Thread
import json
import datetime
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "vk1.a.zidqHJSr_rH16BGRm__NjwiqNHzf-VEp6lo8Ciz6fj11keoYZbpFwaAHJp5UJx8tLGyE76RpPVHP6RcGFuDFRchJyjqmpceYvxkzfcgnIivSnwnff88opI7N43awA_n2AxxpniUJCHOsmds3n5R70ZCIMn1rCHwD55WU7izaFQS6rM5dqF5itvX5EphZ-mIN1BKDNkkErL_EsN3YRS1Tvw"
vk_session = VkApi(token=token)
group_id = 218663113
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()
RickBtn = {"text": "Начать вечеринку", "color": VkKeyboardColor.PRIMARY, "type": "Rick"}


def Write_conversationMessages(peer_id, message, keyboard = None):
    if (keyboard != None):
        keyboard = keyboard.get_keyboard()
    vk.messages.send(random_id=get_random_id(), peer_id=peer_id, message=message, keyboard=keyboard)


def editMsg(event, message):
    vk.messages.edit(
        conversation_message_id=event.obj.conversation_message_id,
        peer_id=event.obj["peer_id"],
        message=message
    )


RickRoll = [
    """⠀⠀⠀⠀⣴⣋⣉⣉⡉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⡃⠟⠛⠛⠛⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠤⣤⠀⠄⠘⣏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⡅⠀⠘⠆⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢶⠠⠷⠀⠓⠣⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢘⣤⡇⠀⡄⣼⣾⣽⣑⣲⣤⣀⠀⠀
⠀⠀⠀⢀⣴⡎⠙⢙⠞⠁⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⣴⣾⣿⣿⣧⣤⡼⠶⣾⣿⣿⣿⣿⣿⣿⣿⣾⠀
⢸⣿⣿⣿⣿⣿⣇⢘⣾⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀
⠈⣿⣿⣿⣿⣿⣿⢘⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⣿⠿⣿⣿⣿⣿⠠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢠⠟⠀⣿⣿⣿⣿⠶⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣏⣀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢿⣿⣿⡿⣿⣿⣿⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢀⢉⣙⣿⢿⣿⣿⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠀""",
    """⣿⣿⣿⣿⠋⠴⠶⠶⢶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠏⢼⣠⣤⣤⣤⡄⠈⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢸⣛⠛⣿⣻⣧⠰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⢺⣿⣧⣹⣿⣿⢈⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣦⡉⣟⣈⣿⣬⣜⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡧⠛⢸⣿⢻⠃⠁⠂⠮⠍⠛⠿⣿⣿
⣿⣿⣿⡿⠋⢱⣦⡦⣡⣾⠀⠀⠀⠀⠀⠀⠀⠘⣿
⣿⠋⠁⠀⠀⠘⠛⢃⣉⠁⠀⠀⠀⠀⠀⠀⠀⠁⣿
⡇⠀⠀⠀⠀⠀⠸⡧⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿
⣷⠀⠀⠀⠀⠀⠀⡧⠄⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿
⣿⠀⣀⠀⠀⠀⠀⣟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
⡟⣠⣿⠀⠀⠀⠀⣉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠰⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡀⠀⠀⢀⠀⠀⠀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡿⡶⠦⠀⡀⠀⠀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⣿"""
]


def StartParty(event):
    while True:
        time.sleep(1)
        editMsg(event, RickRoll[0])
        time.sleep(1)
        editMsg(event, RickRoll[1])


def StartBot():
    while True:
        print("Сервер запущен")
        # Основной цикл
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_EVENT:
                type = event.object.payload["type"]
                if type == "Rick":
                    Thread(target=StartParty, args=(event,)).start()


            elif event.type == VkBotEventType.MESSAGE_NEW:
                request = event.obj["message"]["text"].lower()
                print(request)
                if "rick roll" == request:
                    keyboard = VkKeyboard(inline=True)
                    keyboard.add_callback_button(
                        label=RickBtn["text"],
                        color=RickBtn["color"],
                        payload={"type": RickBtn["type"]}
                    )
                    Write_conversationMessages(event.obj.message["peer_id"], RickRoll[0], keyboard)
                elif "333" in request or "300 30 3" in request:
                    Write_conversationMessages(event.obj.message["peer_id"], "ОГОНЬ!!!")

StartBot()
