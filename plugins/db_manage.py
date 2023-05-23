from plugins.models import User
from pyrogram import Client, filters
import json

def return_user(user_id):
        return User().select().where(user_id).first()

def create_user(user_id):
    if User().get(user_id) != None: return False
    user = User.create(user_id=user_id)
    return True

def update_message(user_id):
        user = return_user(user_id)
        if user == None: return False
        if user != None:
                message = user.messages
                get_messages = json.loads(message)
                print(get_messages)

