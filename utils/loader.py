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
    
    def get_home_guild_ids(self):
        try:
            home_guilds_ids = self.config["HOME_GUILD_IDS"].split(',')
            return list(map(int, home_guilds_ids))
        except:
            raise Exception("Environment variable 'HOME_GUILD_IDS' was not found or its value is not corresponding to the format <int>,<int>!")

    def get_on_ready_channel_ids(self):
        try:
            on_ready_channel_ids = self.config["ON_READY_CHANNEL_IDS"].split(',')
            return list(map(int, on_ready_channel_ids))
        except:
            raise Exception("Environment variable 'ON_READY_CHANNEL_IDS' was not found or its value is not corresponding to the format <int>,<int>!")

    def get_owner_id(self):
        try:
            return int(self.config["OWNER_ID"])
        except:
            raise Exception("Environment variable 'OWNER_ID' was not found or is not integer!")


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
