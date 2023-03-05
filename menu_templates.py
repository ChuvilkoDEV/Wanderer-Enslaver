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

# Генератор простых меню
def menuConstructor(type, buttons, fromId, peerId, isFromUser, attachment = None):
    with open(f'DataBase/menuConfig/{type}.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        config = DB_Commands.selectSettingsByConfig(config, fromId)
        return {
            "message": replaceFString(config["text"], config["data"]),
            "keyboard": generateKeyboard(buttons, isFromUser),
            "peer_id": peerId,
            "attachment": attachment
        }

def aboutMenu(fromId, peerId, fromUser=False):
    buttons = (slavesBtn, skillsBtn, None, inventoryBtn, equipmentBtn, None, jobBtn)
    return menuConstructor('about', buttons, fromId, peerId, fromUser)

def slavesMenu(fromId, peerId, fromUser=False):
    buttons = (slavesJobBtn, slavesFoodBtn, None, aboutBtn)
    return menuConstructor('slaves', buttons, fromId, peerId, fromUser)

def inventoryMenu(fromId, peerId, fromUser=False):
    buttons = (craftBtn, FoodBtn, None, aboutBtn)
    return menuConstructor('inventory', buttons, fromId, peerId, fromUser)

def skillsMenu(fromId, peerId, fromUser=False):
    buttons = (aboutBtn,)
    return menuConstructor('skills', buttons, fromId, peerId, fromUser)

def equipmentMenu(fromId, peerId, fromUser=False):
    buttons = (aboutBtn,)
    return menuConstructor('equipment', buttons, fromId, peerId, fromUser)

def jobMenu(fromId, peerId, fromUser=False):
    buttons = (aboutBtn,)
    return menuConstructor('job', buttons, fromId, peerId, fromUser)
