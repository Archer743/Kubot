import nextcord
from nextcord import Interaction, Member
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot


class Ping(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Provides the latency of the bot.")
    async def ping(self, inter: Interaction, member:Member):
        embed = Embed(
            title="Pong :ping_pong: ",
            description=f"Latency: **{round(self.client.latency * 1000)}**ms",
            color=Color.from_rgb(14, 39, 46)
        )

        return await inter.response.send_message(embed=embed)

def setup(bot: Bot):
    bot.add_cog(Ping(bot))
