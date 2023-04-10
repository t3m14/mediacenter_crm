from peewee import Model, IntegerField

class Chats(Model):
    chat_id = IntegerField(null=False, unique=True, verbose_name="Айди чата")

