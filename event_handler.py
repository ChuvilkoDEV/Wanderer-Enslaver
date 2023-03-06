import BotVk
import menu_templates


def editMsg(data, messageId):
    if data["keyboard"] != None:
        data["keyboard"] = data["keyboard"].get_keyboard()
    BotVk.vk.messages.edit(
        conversation_message_id=messageId,
        peer_id=data["peer_id"],
        message=data["message"],
        attachment=data["attachment"],
        keyboard=data["keyboard"]
    )


def handler(event):
    type = event.object.payload["type"]
    if type == menu_templates.aboutBtn["type"]:  # about
        data = menu_templates.aboutMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.slavesBtn["type"]:  # slaves
        data = menu_templates.slavesMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.inventoryBtn["type"]:  # inventory
        data = menu_templates.inventoryMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.skillsBtn["type"]:  # skills
        data = menu_templates.skillsMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.equipmentBtn["type"]:  # equipment
        data = menu_templates.equipmentMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.jobDebugBtn["type"]:
        menu_templates.jobDebugMenu(event.obj["user_id"])

    elif type == menu_templates.jobBtn["type"]:  # job
        data = menu_templates.jobMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.minesBtn["type"]:  # mines
        data = menu_templates.minesMenu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.stoneMineBtn["type"]:
        data = menu_templates.gotoMine(event.obj["user_id"], event.obj["peer_id"], 1)
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.ironMineBtn["type"]:
        data = menu_templates.gotoMine(event.obj["user_id"], event.obj["peer_id"], 10)
        editMsg(data, event.obj.conversation_message_id)

    elif type == menu_templates.goldMineBtn["type"]:
        data = menu_templates.gotoMine(event.obj["user_id"], event.obj["peer_id"], 50)
        editMsg(data, event.obj.conversation_message_id)


