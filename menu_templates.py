import datetime
import BotVk
from DataBase import DB_Commands
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

aboutBtn = {"text": "Обо мне", "color": VkKeyboardColor.PRIMARY, "type": "about"}
slavesBtn = {"text": "Мои рабы", "color": VkKeyboardColor.PRIMARY, "type": "slaves"}
slavesJobBtn = {"text": "Работа рабов", "color": VkKeyboardColor.PRIMARY, "type": "slavesJob"}
slavesFoodBtn = {"text": "Работа рабов", "color": VkKeyboardColor.PRIMARY, "type": "slavesFood"}
skillsBtn = {"text": "Мои навыки", "color": VkKeyboardColor.PRIMARY, "type": "skills"}
inventoryBtn = {"text": "Мои инвентарь", "color": VkKeyboardColor.PRIMARY, "type": "inventory"}
craftBtn = {"text": "Крафт", "color": VkKeyboardColor.PRIMARY, "type": "craft"}
FoodBtn = {"text": "Рацион питания", "color": VkKeyboardColor.PRIMARY, "type": "Food"}
equipmentBtn = {"text": "Мое снаряжение", "color": VkKeyboardColor.PRIMARY, "type": "equipment"}
jobBtn = {"text": "Работа", "color": VkKeyboardColor.PRIMARY, "type": "job"}
jobRaidBtn = {"text": "В рейд", "color": VkKeyboardColor.PRIMARY, "type": "jobRaid"}
jobMinesBtn = {"text": "В шахты", "color": VkKeyboardColor.PRIMARY, "type": "jobMines"}


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


def generate_keyboard(buttons, fromUser):
    keyboard = VkKeyboard(inline=True)
    if (fromUser):
        return addDefaultBtn(keyboard, buttons)
    else:
        return addCallbackBtn(keyboard, buttons)


def replaceFString(s, data):
    for i in range(len(data)):
        if s.find(f"<<{i}>>"):
            s = s.replace(f"<<{i}>>", str(data[i]))
    return s

def menu_constructor(type, buttons, fromId, peerId, isFromUser, attachment = None):
    data = DB_Commands.select_settings_byConfig(f'DataBase/config/{type}_config.txt', fromId)
    with open(f'DataBase/text/{type}_text.txt', 'r', encoding="utf-8") as f:
        return {
            "message": replaceFString(f.read(), data),
            "keyboard": generate_keyboard(buttons, isFromUser),
            "peer_id": peerId,
            "attachment": attachment
        }

def about_menu(from_id, peer_id, from_user=False):
    buttons = (slavesBtn, skillsBtn, None, inventoryBtn, equipmentBtn, None, jobBtn)
    return menu_constructor('about', buttons, from_id, peer_id, from_user)

def slave_menu(from_id, peer_id, from_user=False):
    buttons = (slavesJobBtn, slavesFoodBtn, None, aboutBtn)
    data = []

    with open('DataBase/text/slaves_text.txt', 'r', encoding="utf-8") as f:
        return {
            "message": replaceFString(f.read(), data),
            "keyboard": generate_keyboard(buttons, from_user),
            "peer_id": peer_id,
            "attachment": None
        }

def inventory_menu(from_id, peer_id, from_user=False):
    buttons = (craftBtn, FoodBtn, None, aboutBtn)
    return menu_constructor('inventory', buttons, from_id, peer_id, from_user)

def skills_menu(from_id, peer_id, from_user=False):
    buttons = (aboutBtn,)
    return menu_constructor('skills', buttons, from_id, peer_id, from_user)

