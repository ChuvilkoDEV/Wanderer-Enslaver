from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import json
import datetime

import message_handler
import event_handler

# API-ключ созданный ранее
token = "vk1.a.lgCaEthdmPhZ1WFFxRBx65D0o4DCanbuSjRETmN-21kj7xd6EUgRX4tsG1J-9ItKmf9cK9aq7SMpXxsvowwFvqH5hn_mXVxzbE1gUvTf-X70xIQqQbsr9x5-AnLc_awVjhPFP1dY7AbDwuSeIYYDqb-iwlSFMnH6PS7s1Gjeb7utzSgcUak1zS2DlaD7xH6sEXbzoNCfv05dDC_vth0icQ"
vk_session = VkApi(token=token)
group_id = 218768066
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

def startBot():
    print("Сервер запущен!")
    while True:
        #try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_EVENT:
                event_handler.handler(event)
            elif event.type == VkBotEventType.MESSAGE_NEW:
                message_handler.handler(event)

        #except Exception as s:
            #print(f"Unexpected: {s}\n{s=}, {type(s)=}")