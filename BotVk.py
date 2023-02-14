from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import json
import datetime

import vk_conversations

# API-ключ созданный ранее
token = "vk1.a.lgCaEthdmPhZ1WFFxRBx65D0o4DCanbuSjRETmN-21kj7xd6EUgRX4tsG1J-9ItKmf9cK9aq7SMpXxsvowwFvqH5hn_mXVxzbE1gUvTf-X70xIQqQbsr9x5-AnLc_awVjhPFP1dY7AbDwuSeIYYDqb-iwlSFMnH6PS7s1Gjeb7utzSgcUak1zS2DlaD7xH6sEXbzoNCfv05dDC_vth0icQ"
vk_session = VkApi(token=token)
group_id = 218768066
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

def Write_conversationMessages(vk, peer_id, message, attachment=None, keyboard=None, template=None):
    if keyboard != None:
        keyboard = keyboard.get_keyboard()
    vk.messages.send(random_id=get_random_id(), peer_id=peer_id, message=message, attachment=attachment, keyboard=keyboard)

def write_PrivateMsg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0})


def startBot():
    try:
        print("Сервер запущен!")
        while True:
            f_toggle: bool = False
            # Основной цикл
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_EVENT:
                    if event.object.payload.get("type") == "my_own_100500_type_edit":
                        vk.messages.edit(
                            peer_id=event.obj.peer_id,
                            message="Меню #2",
                            conversation_message_id=event.obj.conversation_message_id
                        )
                elif event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                    vk_conversations.conversation(event)
                elif event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                    print(event.obj.json())

    except Exception as ex:
        print(ex)