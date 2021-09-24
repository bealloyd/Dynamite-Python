import random

from bot import Bot

class scissorBot(Bot):
    def __init__(self):
        pass

    def make_move(self, gamestate):
        return 'S'
    # print ("get cut")

#
# trashtalk = ["Get cut"]
# # "You didn't make the cut", "Get to the point", "Take this Shearesously"[3], "Stop cutting corners"[4], "This is pointless"[5]]
# outputtrash = trashtalk[random.randint(0, len(trashtalk) - 1)]
#
# win_counter = 0
# while win_counter < 69:
#     print(outputtrash)
#     win_counter += 1