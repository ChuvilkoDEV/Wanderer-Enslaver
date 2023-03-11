import datetime
import BotVk
import json
from DataBase import DB_Commands as DB
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

aboutBtn = {"text": "Обо мне", "color": VkKeyboardColor.PRIMARY, "type": "about"}

slavesBtn = {"text": "Мои рабы Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "slaves"}
slavesJobBtn = {"text": "Еда рабов Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "slavesJob"}
slavesFoodBtn = {"text": "Работа рабов Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "slavesFood"}

skillsBtn = {"text": "Мои навыки", "color": VkKeyboardColor.PRIMARY, "type": "skills"}
equipmentBtn = {"text": "Мое снаряжение", "color": VkKeyboardColor.PRIMARY, "type": "equipment"}

inventoryBtn = {"text": "Мои инвентарь", "color": VkKeyboardColor.PRIMARY, "type": "inventory"}
craftBtn = {"text": "Крафт Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "craft"}
foodBtn = {"text": "Рацион питания Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "Food"}

jobBtn = {"text": "Работа", "color": VkKeyboardColor.PRIMARY, "type": "job"}
abortJobBtn = {"text": "Прервать работу", "color": VkKeyboardColor.PRIMARY, "type": "abortJob"}

minesBtn = {"text": "В шахты", "color": VkKeyboardColor.PRIMARY, "type": "mines"}
stoneMineBtn = {"text": "Каменная шахта", "color": VkKeyboardColor.PRIMARY, "type": "stoneMine"}
ironMineBtn = {"text": "Железная шахта", "color": VkKeyboardColor.PRIMARY, "type": "ironMine"}
goldMineBtn = {"text": "Золотая шахта", "color": VkKeyboardColor.PRIMARY, "type": "goldMine"}

wastelandBtn = {"text": "В Пустошь Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "wasteland"}
outpostBtn = {"text": "Атаковать форпосты Н/Р", "color": VkKeyboardColor.PRIMARY, "type": "outpost"}


def addCallbackBtn(keyboard, buttons):
    for i in buttons:
        if i is None:
            keyboard.add_line()
        else:
            keyboard.add_callback_button(
                label=i["text"],
                color=i["color"],
                payload={"type": i["type"]}
            )
    return keyboard


def addDefaultBtn(keyboard, buttons):
    for i in buttons:
        if i is None:
            keyboard.add_line()
        else:
            keyboard.add_callback_button(
                label=i["text"],
                color=i["color"],
                payload={"type": i["type"]}
            )
    return keyboard


def generateKeyboard(buttons, fromUser):
    keyboard = VkKeyboard(inline=True)
    if fromUser:
        return addDefaultBtn(keyboard, buttons)
    else:
        return addCallbackBtn(keyboard, buttons)


def replaceFString(s, data):
    if data is None:
        return
    for i in data:
        if s.find(f"<<{i}>>"):
            s = s.replace(f"<<{i}>>", str(data[i]))
    return s


def selectConfig(type, fromId):
    with open(f'DataBase/menuConfig/{type}.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return DB.selectSettingsByConfig(config, fromId)


# Генератор простых меню
def menuConstructor(config, buttons, peerId, isFromUser, textId='default', attachment=None):
    return {
        "message": replaceFString(config["text"][textId], config["data"]),
        "keyboard": generateKeyboard(buttons, isFromUser),
        "peer_id": peerId,
        "attachment": attachment
    }


def aboutMenu(fromId, peerId, isFromUser=False):
    buttons = (slavesBtn, skillsBtn, None, inventoryBtn, equipmentBtn, None, jobBtn)
    config = selectConfig(aboutBtn["type"], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser)


def slavesMenu(fromId, peerId, isFromUser=False):
    buttons = (slavesJobBtn, slavesFoodBtn, None, aboutBtn)
    config = selectConfig(slavesBtn["type"], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser)


def inventoryMenu(fromId, peerId, isFromUser=False):
    buttons = (craftBtn, foodBtn, None, aboutBtn)
    config = selectConfig(inventoryBtn["type"], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser)


def skillsMenu(fromId, peerId, isFromUser=False):
    buttons = (aboutBtn,)
    config = selectConfig(skillsBtn["type"], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser)


def equipmentMenu(fromId, peerId, isFromUser=False):
    buttons = (aboutBtn,)
    config = selectConfig(equipmentBtn["type"], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser)


def jobMenu(fromId, peerId, isFromUser=False):
    config = selectConfig(jobBtn["type"], fromId)
    config["data"]["nextWork"] = DB.strToDatetime(config["data"]["nextWork"])
    config["data"]["workEnd"] = DB.strToDatetime(config["data"]["workEnd"])
    now = datetime.datetime.now()

    if config["data"]["isOnWork"] == 1 and config["data"]["workEnd"] >= now:
        buttons = (aboutBtn, abortJobBtn)
        delta = config["data"]["workEnd"] - now
        config["data"]["hours"] = delta.seconds // 3600
        config["data"]["minutes"] = (delta.seconds % 3600) // 60
        return menuConstructor(config, buttons, peerId, isFromUser, "onWork")
    elif config["data"]["isOnWork"] == 1 and config["data"]["workEnd"] < now:
        buttons = (jobBtn,)
        DB.insertSettingsByConfig(config["setToDB"], [0], fromId)
        return menuConstructor(config, buttons, peerId, isFromUser, "endWork")
    elif config["data"]["nextWork"] >= now:
        buttons = (aboutBtn,)
        delta = config["data"]["nextWork"] - now
        config["data"]["hours"] = delta.seconds // 3600
        config["data"]["minutes"] = (delta.seconds % 3600) // 60
        return menuConstructor(config, buttons, peerId, isFromUser, "chillTime")
    else:
        buttons = (wastelandBtn, outpostBtn, minesBtn, None, aboutBtn)
        return menuConstructor(config, buttons, peerId, isFromUser, "canWork")


def abortJobMenu(fromId, peerId, isFromUser=False):
    buttons = (wastelandBtn, outpostBtn, minesBtn, None, aboutBtn)
    config = selectConfig(jobBtn["type"], fromId)
    time = datetime.datetime.now()
    DB.insertSettingsByConfig("Update users set nextWork = ?, workEnd = ?, isOnWork = ? where user_id = ?", [DB.DatetimeToStr(time), DB.DatetimeToStr(time), 0], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser, "canWork")

def minesMenu(fromId, peerId, isFromUser=False):
    buttons = (stoneMineBtn, ironMineBtn, goldMineBtn, None, jobBtn)
    config = selectConfig(minesBtn["type"], fromId)
    return menuConstructor(config, buttons, peerId, isFromUser)


def gotoMine(fromId, peerId, level, isFromUser=False):
    config = selectConfig("gotoMine", fromId)
    config["data"]["nextWork"] = DB.strToDatetime(config["data"]["nextWork"])

    if config["data"]["nextWork"] > datetime.datetime.now():
        buttons = (aboutBtn,)
        return menuConstructor(config, buttons, peerId, isFromUser, "timeErr")
    elif config["data"]["employment"] < level:
        buttons = (jobBtn,)
        return menuConstructor(config, buttons, peerId, isFromUser, "lowLevel")
    else:
        buttons = (aboutBtn,)
        workEnd = DB.DatetimeToStr(datetime.datetime.now() + datetime.timedelta(hours=1))
        nextWork = DB.DatetimeToStr(datetime.datetime.now() + datetime.timedelta(hours=5))
        DB.insertSettingsByConfig(config["setToDB"], [nextWork, workEnd, 1], fromId)
        return menuConstructor(config, buttons, peerId, isFromUser, "success")


