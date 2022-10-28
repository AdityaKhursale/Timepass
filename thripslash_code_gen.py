from datetime import datetime
import pywhatkit
import random

players = [
    "+1XXXXXXXXXX"
]

currentTime = datetime.now()
print(currentTime.minute, currentTime.hour)
msgPrefix = "Your username for today's game is - "
for player in players:
    pywhatkit.sendwhatmsg_instantly(
        player,
        "{}{}".format(msgPrefix, random.randint(1111, 9999))
    )
