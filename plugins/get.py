from requests.exceptions import HTTPError

import pypokedex
from pyrogram.types import (
    InputMediaPhoto,
)

from .utils import get_caption, STICKER_ID

def send_msg(p, message):

    photo = p.sprites.front.get("shiny")
    ms = message.reply_text(
        text=" Please wait a second, your content is loading"
    )

    message.reply_sticker(
        sticker=STICKER_ID
    )

    message.reply_media_group(
        [
            InputMediaPhoto(
                photo,
                caption=get_caption(p)
            ),
            InputMediaPhoto(p.sprites.back.get("shiny")),
        ]
    )
    ms.edit_text("Your content is ready")

def send(client, message):
    try:
        p = pypokedex.get(dex=int(message.text))
    except ValueError:
        p = pypokedex.get(name=message.text)
    except HTTPError as e:
        message.reply_text(text="Sorry, an error has occured.")
        raise HTTPError(e)
    send_msg(p, message)