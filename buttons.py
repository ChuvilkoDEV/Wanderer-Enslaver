from vk_api.keyboard import VkKeyboard, VkKeyboardColor

aboutBtn = {"text":"Обо мне", "color":VkKeyboardColor.PRIMARY, "type":"about"}
slavesBtn = {"text":"Мои рабы", "color":VkKeyboardColor.PRIMARY, "type":"slaves"}
skillsBtn = {"text":"Мои навыки", "color":VkKeyboardColor.PRIMARY, "type":"skills"}
inventoryBtn = {"text":"Мои инвентарь", "color":VkKeyboardColor.PRIMARY, "type":"inventory"}
equipmentBtn = {"text":"Мое снаряжение", "color":VkKeyboardColor.PRIMARY, "type":"equipment"}
jobBtn = {"text":"Работа", "color":VkKeyboardColor.PRIMARY, "type":"job"}

def addButtons(keyboard, buttons):
    for i in buttons:
        if (i == None):
            keyboard.add_line()
        else:
            keyboard.add_callback_button(
                label= i["text"],
                color= i["color"],
                payload={"type": i["type"]}
            )
    return keyboard
