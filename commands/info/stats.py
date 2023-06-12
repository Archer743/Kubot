import nextcord
from nextcord import Interaction
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot


class Stats(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="If you want to see this bot's stats, this is the way to do it.")
    async def stats(self, inter: Interaction):
        users, channels = 0, 0

        for server in self.bot.guilds:
            users += server.member_count
            channels += len(server.channels)
   
        embed = Embed(title="Statistics :bar_chart: ", color=Color.from_rgb(14, 39, 46))

        embed.add_field(name='Name', value=f"```{self.bot.user.name}```", inline=True)
        embed.add_field(name='Ping', value=f"```{round(self.bot.latency * 1000)}ms```")

        embed.add_field(name='Servers', value=f"```{len(self.bot.guilds)}```", inline=True)
        embed.add_field(name='Channels', value=f'```{channels}```', inline=True)
        embed.add_field(name='Users', value=f'```{users}```', inline=True)
        
        embed.add_field(name='ID', value=f'```{self.bot.user.id}```', inline=True)
        embed.add_field(name='In Voice Channel?', value='```{}```'.format("Yes" if inter.guild.me.voice != None else "No"), inline=True)

        return await inter.response.send_message(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Stats(bot))
