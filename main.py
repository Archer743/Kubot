from utils.bot import Bot

if __name__ == "__main__":
    bot = Bot()
    bot.loader.load_all()
    bot.run(bot.loader.config["TOKEN"])