from utils.bot import Bot
from os import system

system("color")

if __name__ == "__main__":
    bot = Bot()
    bot.loader.load_all()
    bot.run(bot.loader.config["TOKEN"])
