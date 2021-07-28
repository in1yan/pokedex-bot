import pypokedex
from pyrogram.types import (
    InputMediaPhoto,
)


def send(client, message):
    try:
        p = pypokedex.get(dex=int(message.text))
        photo = p.sprites.front.get("shiny")
        index = p.dex
        height = p.height
        name = p.name
        weight = p.weight
        types = [p.types]
        base = p.base_stats

        ms = message.reply_text(
            text=" Please wait a second ,your content is loading...."
        )
        message.reply_sticker(
            sticker="CAACAgIAAx0CRu5C5QACCMhgsOU_MMxETwbQwARhNAQ2tTzLNQACtgIAAjZ2IA7n32q5Z54wcR8E"
        )
        message.reply_media_group(
            [
                InputMediaPhoto(
                    photo,
                    caption="Name : {} \n".format(name)
                    + "index number : {}\n".format(index)
                    + "Height : {} \n".format(height)
                    + "Weight : {} \n".format(weight)
                    + "Type : {}\n".format(*types, sep="',")
                    + "Base stats : \n "
                    + "\t hp : {}\n".format(p.base_stats.hp)
                    + "\t attack : {} \n".format(p.base_stats.attack)
                    + "\t defence : {} \n".format(p.base_stats.defense)
                    + "\t speed : {} \n".format(p.base_stats.speed),
                ),
                InputMediaPhoto(p.sprites.back.get("shiny")),
            ]
        )
        ms.edit_text("your content is now loaded")
        # send a pokemon on name
    except:
        p = pypokedex.get(name=message.text)
        photo = p.sprites.front.get("shiny")
        index = p.dex
        height = p.height
        name = p.name
        weight = p.weight
        types = [p.types]
        base = p.base_stats

        ms = message.reply_text(
            text=" Please wait a second ,your content is loading...."
        )
        message.reply_sticker(
            sticker="CAACAgIAAx0CRu5C5QACCMhgsOU_MMxETwbQwARhNAQ2tTzLNQACtgIAAjZ2IA7n32q5Z54wcR8E"
        )
        message.reply_media_group(
            [
                InputMediaPhoto(
                    photo,
                    caption="Name : {} \n".format(name)
                    + "index number : {}\n".format(index)
                    + "Height : {} \n".format(height)
                    + "Weight : {} \n".format(weight)
                    + "Type : {}\n".format(*types, sep="',")
                    + "Base stats : \n "
                    + "\t hp : {}\n".format(p.base_stats.hp)
                    + "\t attack : {} \n".format(p.base_stats.attack)
                    + "\t defence : {} \n".format(p.base_stats.defense)
                    + "\t speed : {} \n".format(p.base_stats.speed),
                ),
                InputMediaPhoto(p.sprites.back.get("shiny")),
            ]
        )
        ms.edit_text("your content is now loaded")
