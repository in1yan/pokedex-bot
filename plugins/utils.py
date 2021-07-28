BOT_NAME = '@pokiedex_bot'

STICKER_ID = "CAACAgIAAx0CRu5C5QACCMhgsOU_MMxETwbQwARhNAQ2tTzLNQACtgIAAjZ2IA7n32q5Z54wcR8E"

def get_caption(p):
    return (f"""
Index number: {p.dex}
Name: {p.name}

Height: {p.height}
Weight: {p.weight}

Type: {p.types}

Base stats:
HP: {p.base_stats.hp}
Attack: {p.base_stats.attack}
Defense: {p.base_stats.defense}
Speed: {p.base_stats.speed}
    """)