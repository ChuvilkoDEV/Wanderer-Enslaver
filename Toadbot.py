import time

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from threading import Thread
import json
import datetime

# API-ключ созданный ранее
token = "vk1.a.zidqHJSr_rH16BGRm__NjwiqNHzf-VEp6lo8Ciz6fj11keoYZbpFwaAHJp5UJx8tLGyE76RpPVHP6RcGFuDFRchJyjqmpceYvxkzfcgnIivSnwnff88opI7N43awA_n2AxxpniUJCHOsmds3n5R70ZCIMn1rCHwD55WU7izaFQS6rM5dqF5itvX5EphZ-mIN1BKDNkkErL_EsN3YRS1Tvw"
vk_session = VkApi(token=token)
group_id = 218663113
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()
upload = VkUpload(vk)
'''photo = upload.photo_messages('1675776602227.gif')
owner_id = photo[0]['owner_id']
photo_id = photo[0]['id']
access_key = photo[0]['access_key']
attachment = f'photo{owner_id}_{photo_id}_{access_key}'
print(attachment)
'''
queue = []

def add_Hours(hours):
    return datetime.timedelta(0,0,0,0,0,hours)


def str_to_datetime(date_time_str):
    return datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')


def datetime_to_str(date_time):
    return "{0:%Y-%m-%d %H:%M}".format(date_time)


def push_Queue(Name, time, event_obj):
    Job = {"Name": Name,
           "Time": datetime_to_str(time),
           "Peer_id": event_obj.message["peer_id"],
           "From_id": event_obj.message["from_id"]}
    queue.append(Job)


def write_PrivateMsg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0})


def Write_conversationMessages(vk, peer_id, message, attachment=None):
    vk.messages.send(random_id=get_random_id(), peer_id=peer_id, message=message, attachment=attachment)


def startBot():
    try:
        while True:
            print("Сервер запущен")
            # Основной цикл
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                    request = event.obj["message"]["text"].lower()

                    if "пожелай ей удачи" in request:
                        Write_conversationMessages(vk, event.obj.message["peer_id"], "Я желаю тебе удачи, пусть твой путь к успеху будет легким и быстрым! Пусть все сложится так, как запланировано, поверь в свои силы и талант, смело двигайся вперед. Желаю тебе оптимизма и бодрости, верю, что ты преодолеешь все преграды и добьешься желанной цели!")
                    elif "333" in request or "300 30 3" in request:
                        Write_conversationMessages(vk, event.obj.message["peer_id"], "ОГОНЬ!!!", "https://media.tenor.com/ElljI7mYBTQAAAAC/explosion-movie-set.gif")

                elif event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                    write_PrivateMsg(id, 'Test message')
    except Exception as ex:
        print(ex)

def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )



Thread(target=startBot).start()
