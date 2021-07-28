from pyrogram import client
from pyrogram.types import InlineQueryResultPhoto
import pypokedex

from .utils import get_caption


def answer(client, inline_query):
    p = pypokedex.get(dex=int(inline_query["query"]))

    inline_query.answer(
        results=[
            InlineQueryResultPhoto(
                title=p.name,
                photo_url=p.sprites.front.get("shiny"),
                caption=get_caption(p),
                description="info about pokemon",
                thumb_url=p.sprites.front.get("shiny"),
                ),
        ],
        cache_time=1,
    )
