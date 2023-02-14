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

def about_Person(event):
    data = menu_templates.about_Person(event.obj["user_id"], event.obj["peer_id"])
    editMsg(data, event.obj.conversation_message_id)

def handler(event):
    type = event.object.payload["type"]
    if type == "about":
        about_Person(event)