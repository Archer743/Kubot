import nextcord
from nextcord import Interaction, Member
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot


class ResetNick(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Resets member's nickname in this server")
    async def reset_nick(self, inter: Interaction, member:Member):
        if not (inter.user.guild_permissions.change_nickname and inter.user.guild_permissions.manage_nicknames):
            return await inter.response.send_message("You don't have 'change_nickname' or 'manage_nicknames' permission!")
        
        try:
            if member.nick == None:
                return await inter.response.send_message(f"```{member} already has a default nickname!```")
            
            await member.edit(nick=None)

            embed=Embed(
                title="Nick Reset :pencil:",
                color=Color.from_rgb(14, 39, 46)
            ).add_field(name="Member", value=f"```{member}```", inline=True
            ).add_field(name="New Nick", value=f"```{member.nick}```")

            return await inter.response.send_message(embed=embed)

        except:
            return await inter.response.send_message(f"```For some reason I can't do this!```")


def setup(bot: Bot):
    bot.add_cog(ResetNick(bot))
