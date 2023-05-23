from pyrogram import Client,filters
from . import var
from plugins.db_manage import *

@Client.on_message(filters.regex(r"^(?!\/\w+).+"))
def forward(client,message):
        user_id = message.chat.id
        msg = message.text 
        message.reply_text(var.forward_message)
        client.send_message(var.admin,f"{msg} \n {user_id}\n {message.from_user.id}")
        update_message(user_id=user_id)