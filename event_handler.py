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
    if type == "about":
        data = menu_templates.about_menu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == "slaves":
        data = menu_templates.slave_menu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == "inventory":
        data = menu_templates.inventory_menu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == "skills":
        data = menu_templates.skills_menu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

    elif type == "job":
        data = menu_templates.job_menu(event.obj["user_id"], event.obj["peer_id"])
        editMsg(data, event.obj.conversation_message_id)

