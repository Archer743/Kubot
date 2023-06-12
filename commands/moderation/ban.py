import nextcord
from nextcord import Interaction, Member
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot
import datetime


class Ban(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Given member of this server is banned from it")
    async def ban(self, inter: Interaction, member:Member, reason:str=None):
        if not (inter.user.guild_permissions.ban_members and inter.user.guild_permissions.manage_roles):
            return await inter.response.send_message("You don't have 'ban_members' or 'manage_roles' permission!")

        if member.id == self.bot.user.id:
            return await inter.response.send_message(f"```I can't ban myself!```")
        
        if member.id == inter.user.id:
            return await inter.response.send_message(f"```You can't ban yourself!```")

        if member.top_role >= inter.user.top_role:
            return await inter.response.send_message(f"```You can't ban this user!```")

        try:
            reason = None if reason == None else reason[:512]
            await member.ban(reason=reason)

            embed = Embed(title="Ban :hammer:", color=Color.from_rgb(14, 39, 46))
            embed.add_field(name="Member", value=f"```{member.name}```", inline=False)
            embed.add_field(name="Banned At", value="```{}```".format(datetime.datetime.now().strftime("%a, %#d %B %Y, %I:%M %p, UTC")), inline=False)
            embed.add_field(name="Reason", value="```{}```".format(reason), inline=False)

            return await inter.response.send_message(embed=embed)
            
        except:
            return await inter.response.send_message(f"```For some reason I can't do this!```")


def setup(bot: Bot):
    bot.add_cog(Ban(bot))
