from pyrogram import Client,filters
from . import var

@Client.on_message(filters.regex(r"^(?!\/\w+).+"))
def forward(client,message):
        msg = message.text 
        message.reply_text(var.forward_message)
        client.send_message(var.admin,f"{msg} \n {message.from_user.id}")