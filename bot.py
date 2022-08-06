from plugins.inline import answer
from plugins.random import rand
from plugins.get import send
from pyrogram import Client, filters,emoji

from plugins.utils import BOT_NAME


app = Client("pokedex", config_file="config.ini",parse_mode = 'html')

# start command
@app.on_message(filters.command(["start"]))
def start_command(client, message):

    message.reply_text(
       f"""
{emoji.SPARKLES} Hello {message.from_user.mention} {emoji.SPARKLES},
I am a pokedex bot.

Send any pokemon name or index number and I will send the info about the pokemon. {emoji.SCROLL}

You can also call me inline:
{BOT_NAME} followed by the index number.

Type /help to know how to use me.
""",)

# help command
@app.on_message(filters.command(["help"]))
def help_command(client, message):
    message.reply_text(f"""
Just send the name of the pokemon or its index number, I will search for the pokemon and send it to you.

For example:
type {BOT_NAME} 25 and I wil send you Pikachu as result.

You can also call me inline by typing @pokiedex_bot followed by index number.
In inline mode only supports index number.
    """)

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
