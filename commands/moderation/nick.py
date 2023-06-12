import nextcord
from nextcord import Interaction, Member
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot


class Nick(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Changes member's nick in this server")
    async def nick(self, inter: Interaction, member:Member, nick:str):
        if not inter.user.guild_permissions.manage_nicknames:
            return await inter.response.send_message("You don't have 'manage_nicknames' permission!")
        
        try:
            if nick == member.nick or nick == member.name:
                return await inter.response.send_message(f"```{member} already has that nickname!```")

            elif len(nick) > 32:
                return await inter.response.send_message(f"```Nickname length must be less than ***32***```")
            
            await member.edit(nick=nick)

            embed=Embed(
                title="New Nick :pencil:",
                color=Color.from_rgb(14, 39, 46)
            ).add_field(name="Member", value=f"```{member}```", inline=True
            ).add_field(name="New Nick", value=f"```{nick}```")

            return await inter.response.send_message(embed=embed)
        
        except:
            return await inter.response.send_message(f"```For some reason I can't do this!```")


def setup(bot: Bot):
    bot.add_cog(Nick(bot))
