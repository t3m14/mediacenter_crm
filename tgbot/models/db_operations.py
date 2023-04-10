from peewee import SqliteDatabase
from models import *
db = SqliteDatabase("../../database.db")

def create_chat(chat_id):
    exists = False
    try:
        chat = Chats.select().where(
            Chats.chat_id == chat_id
            ).get()
        return False
    except:
        if not exists:
            row = Chats(
                chat_id=chat_id
            )
            row.save()
            return True
def delete_chat(chat_id):
    try:
        chat = Chats.select().where(
            Chats.chat_id == chat_id
            ).get()
        return True
    except: return False
def init():
    db.connect()
    Chats.create_table()
    