from pyrogram import Client,filters
from plugins.models import User
from . import var

# @Client.on_message(filters.create(lambda flt, client, update: utils.check_status(update, 'NORMAL')) &
# 	filters.private &
# 	filters.user(var.SUDO) &
# 	filters.text &
# 	~filters.command("userList"))

# def userList(client,message):
#     message.reply_text(User())
    
