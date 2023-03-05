import datetime
import BotVk
import json
from DataBase import DB_Commands
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

aboutBtn = {"text": "Обо мне", "color": VkKeyboardColor.PRIMARY, "type": "about"}
slavesBtn = {"text": "Мои рабы Н/А", "color": VkKeyboardColor.PRIMARY, "type": "slaves"}
slavesJobBtn = {"text": "Еда рабов Н/А", "color": VkKeyboardColor.PRIMARY, "type": "slavesJob"}
slavesFoodBtn = {"text": "Работа рабов Н/А", "color": VkKeyboardColor.PRIMARY, "type": "slavesFood"}
skillsBtn = {"text": "Мои навыки", "color": VkKeyboardColor.PRIMARY, "type": "skills"}
inventoryBtn = {"text": "Мои инвентарь", "color": VkKeyboardColor.PRIMARY, "type": "inventory"}
craftBtn = {"text": "Крафт Н/А", "color": VkKeyboardColor.PRIMARY, "type": "craft"}
FoodBtn = {"text": "Рацион питания Н/А", "color": VkKeyboardColor.PRIMARY, "type": "Food"}
equipmentBtn = {"text": "Мое снаряжение", "color": VkKeyboardColor.PRIMARY, "type": "equipment"}
jobBtn = {"text": "Работа Н/А", "color": VkKeyboardColor.PRIMARY, "type": "job"}
jobRaidBtn = {"text": "В рейд Н/А", "color": VkKeyboardColor.PRIMARY, "type": "jobRaid"}
jobMinesBtn = {"text": "В шахты Н/А", "color": VkKeyboardColor.PRIMARY, "type": "jobMines"}


def addCallbackBtn(keyboard, buttons):
    for i in buttons:
        if (i == None):
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
        if (i == None):
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
    if (fromUser):
        return addDefaultBtn(keyboard, buttons)
    else:
        return addCallbackBtn(keyboard, buttons)


def replaceFString(s, data):
    if (data == None):
        return
    for i in data:
        if s.find(f"<<{i}>>"):
            s = s.replace(f"<<{i}>>", str(data[i]))
    return s


def selectConfig(type, fromId):
    with open(f'DataBase/menuConfig/{type}.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return DB_Commands.selectSettingsByConfig(config, fromId)


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
    buttons = (craftBtn, FoodBtn, None, aboutBtn)
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
    buttons = (aboutBtn,)
    config = selectConfig(jobBtn["type"], fromId)
    config["data"]["time_for_next_job"] = datetime.datetime.strptime(
        config["data"]["time_for_next_job"],
        '%Y-%m-%d %H:%M:%S.%f'
    )
    if (datetime.datetime.now() >= config["data"]["time_for_next_job"]):
        return menuConstructor(config, buttons, peerId, isFromUser, "canWork")
    else:
        return menuConstructor(config, buttons, peerId, isFromUser, "canNotWork")
