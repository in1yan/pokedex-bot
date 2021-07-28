import random

import pypokedex
import tgcrypto
from plugins.inline import answer
from plugins.random import rand
from plugins.get import send
from pyrogram import Client, filters,emoji
from pyrogram.types import (
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

app = Client("pokedex", config_file="config.ini",parse_mode = 'html')

# start command
@app.on_message(filters.command(["start"]))
def start_command(client, message):
   
    start_msg = f"""

{emoji.SPARKLES} Hello {message.from_user.mention} {emoji.SPARKLES}, 
I am a pokedex bot 
send any pokemon name or index number 
I wil send pokemon satats  {emoji.SCROLL}
you can also call it inline:
        @pokiedex_bot and then index number
see /help :
    To know how to use me...

"""
   message.reply_text(
       start_msg,
   )


# help command
@app.on_message(filters.command(["help"]))
def help_command(client, message):
    message.reply_text(
        "just send the name fo the pokemon or it index number , I will search for the pokemon and send it to you"
        + "\nyou can also call me inline by typing @pokiedex_bot"
        + "\nfor example:"
        + "\ntype (@pokiedex_bot 25) \nit wil send you pikachu as result"
        + "\nnote:"
        + "\n\tIn inline mode It only support index number ."
    )



# send a random pokemon
@app.on_message(filters.command(["random"]))
def random_command(client, message):
    rand(client, message)


# send a pokemon on index number or by name
@app.on_message(filters.private & filters.text)
def send_pokemon(client, message):
     send(client, message)
 

@app.on_inline_query()
def ans(client, inline_query):

    answer(client, inline_query)


app.run()
