import random
import pypokedex
from pyrogram.types import (
    InputMediaPhoto,
)

from .utils import get_caption, STICKER_ID

def rand(client, message):
    message.reply_sticker(
        sticker=STICKER_ID
    )

    choice = list(range(1, 901))
    p = pypokedex.get(dex=random.choice(choice))
    photo = p.sprites.front.get("shiny")

    ms = message.reply_text(text=" Please wait a second ,your content is loading...")

    message.reply_media_group(
        [
            InputMediaPhoto(
                photo,
                caption=get_caption(p)
            ),
            InputMediaPhoto(p.sprites.back.get("shiny")),
        ]
    )

    ms.edit_text("your content  is now loaded")