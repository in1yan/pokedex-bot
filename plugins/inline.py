from pyrogram import client, filters
from pyrogram.types import (
    InlineQueryResultPhoto,
    InputMediaPhoto,
)
import pypokedex


def answer(client, inline_query):
    num = list(range(1, 901))
    p = pypokedex.get(dex=int(inline_query["query"]))

    inline_query.answer(
        results=[
            InlineQueryResultPhoto(
                title=p.name,
                photo_url=p.sprites.front.get("shiny"),
                caption="Name : {} \n".format(p.name)
                + "index number : {}\n".format(p.dex)
                + "Height : {} \n".format(p.height)
                + "Weight : {} \n".format(p.weight)
                + "Type : {}\n".format(*p.types, sep="',")
                + "Base stats : \n "
                + "\t hp : {}\n".format(p.base_stats.hp)
                + "\t attack : {} \n".format(p.base_stats.attack)
                + "\t defence : {} \n".format(p.base_stats.defense)
                + "\t speed : {} \n".format(
                    p.base_stats.speed,
                    description="info about pokemon",
                    thumb_url=p.sprites.front.get("shiny"),
                ),
            ),
        ],
        cache_time=1,
    )
