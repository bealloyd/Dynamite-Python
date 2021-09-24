from pprint import pprint

from game import Game
from paperbot import PaperBot
from rockbot import RockBot
from scissorbea import scissorBot
from randombea import Randombot
from otherrandombea import Otherrandombot

def main():
  bot1 = Otherrandombot()
  bot2 = Randombot()
  game = Game(bot1, bot2)
  result = game.play()
  pprint(result)

if __name__ == '__main__':
  main()