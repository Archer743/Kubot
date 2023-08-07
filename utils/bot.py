from nextcord import Intents
from nextcord.ext import commands
from utils.loader import Loader


class Bot(commands.Bot):
    def __init__(self):
        self.loader = Loader(self)
        self.home_guild_ids = self.loader.get_home_guild_ids()
        self.on_ready_channel_ids = self.loader.get_on_ready_channel_ids()

        super().__init__(command_prefix="MCu_!s_THe_B_sT_",
                         intents=Intents.all(),
                         default_guild_ids=self.home_guild_ids)
