import pywhatkit
import random

players = [
    "+1XXXXXXXXXX"
]

msgPrefix = "Your username for today's game is - "
for player in players:
    pywhatkit.sendwhatmsg_instantly(
        player,
        "{}{}".format(msgPrefix, random.randint(1111, 9999))
    )
