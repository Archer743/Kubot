from nextcord import Intents
from nextcord.ext import commands
from data.loader import Loader

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="MCu_!s_THe_B_sT_",
                        intents=Intents.all(),
                        default_guild_ids=[889168117597605918])
        self.loader = Loader(self)