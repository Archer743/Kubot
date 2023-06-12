from dotenv import dotenv_values, find_dotenv
from os import listdir
from termcolor import colored
from nextcord.ext.commands import Bot


class Loader:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.config = dotenv_values(find_dotenv())
        self.loaded_commands = 0
        self.loaded_events = 0

    def load_all(self):
        self.load_commands()
        self.load_events()

        col_text = colored(
            text=f"Loaded {self.loaded_commands} command(s) and {self.loaded_events} event(s)",
            color="green")

        print(col_text)

    def load_commands(self):
        counter = 0

        for folder in listdir("./commands"):
            for file in listdir(f"./commands/{folder}"):
                if file.endswith(".py"):
                    self.bot.load_extension(f"commands.{folder}.{file[:-3]}")
                    counter += 1

            if not counter:
                continue

            self.loaded_commands += counter
            counter = 0

    def load_events(self):
        for file in listdir("./events"):
            if file.endswith(".py"):
                self.bot.load_extension(f"events.{file[:-3]}")
                self.loaded_events += 1
