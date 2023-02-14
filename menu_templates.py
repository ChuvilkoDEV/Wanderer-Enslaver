import datetime
import BotVk
from DataBase import DB_Commands
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

aboutBtn = {"text": "Обо мне", "color": VkKeyboardColor.PRIMARY, "type": "about"}
slavesBtn = {"text": "Мои рабы", "color": VkKeyboardColor.PRIMARY, "type": "slaves"}
skillsBtn = {"text": "Мои навыки", "color": VkKeyboardColor.PRIMARY, "type": "skills"}
inventoryBtn = {"text": "Мои инвентарь", "color": VkKeyboardColor.PRIMARY, "type": "inventory"}
equipmentBtn = {"text": "Мое снаряжение", "color": VkKeyboardColor.PRIMARY, "type": "equipment"}
jobBtn = {"text": "Работа", "color": VkKeyboardColor.PRIMARY, "type": "job"}


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


def about_Person(from_id, peer_id, from_user=False):
    buttons = (aboutBtn, skillsBtn, None, inventoryBtn, equipmentBtn, None, jobBtn)
    data = DB_Commands.select_AboutSettings_user_db(from_id)

    with open('DataBase/text/about_text.txt', 'r', encoding="utf-8") as f:
        return {
            "message": replaceFString(f.read(), data),
            "keyboard": generate_keyboard(buttons, from_user),
            "peer_id": peer_id,
            "attachment": None
        }
