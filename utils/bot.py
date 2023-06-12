from nextcord import Intents
from nextcord.ext import commands
from utils.loader import Loader


class Bot(commands.Bot):
    def __init__(self):
        self.loader = Loader(self)
        super().__init__(command_prefix="MCu_!s_THe_B_sT_",
                         intents=Intents.all(),
                         default_guild_ids=[int(self.loader.config["HOME_SERVER_ID"])])
