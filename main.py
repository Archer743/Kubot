from utils.Bot import Bot

if __name__ == "__main__":
    bot = Bot()
    bot.loader.load_all()
    bot.run(bot.loader.config[mode])