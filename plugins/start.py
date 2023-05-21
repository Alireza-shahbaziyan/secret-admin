from pyrogram import Client,filters
from plugins.models import User
from . import var

@Client.on_message(filters.command('start'))
def start(client,message):
        message.reply_text(var.hello_message)
        try:
            User.create(user_id=message.chat.id,name=message.from_user.first_name)
        except:
                print("User.create Error ./plugins/start.py Line-9")