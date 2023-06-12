import nextcord
from nextcord import Interaction, Member
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot


class Profile(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Provides member's information from the current server.")
    async def profile(self, inter: Interaction, member:Member):
        embed=Embed(color=member.top_role.color)
        embed.set_thumbnail(url=member.avatar.url)

        status_text, status_title = "", ""
        if str(member.raw_status) == "dnd":
            status_text = "Do Not Disturb"
            status_title = "Status :red_circle:"
        elif str(member.raw_status) == "idle":
            status_text = "Idle"
            status_title = "Status :crescent_moon:"
        elif str(member.raw_status) == "online":
            status_text = "Online"
            status_title = "Status :green_circle:"
        else:
            status_text = "Offline"
            status_title = "Status :white_circle:"

        embed.add_field(name="Username", value=f"```{member}```", inline=True)
        embed.add_field(name=f"{status_title}", value=f"```{status_text}```", inline=True)
        embed.add_field(name="Roles", value=f"```{len(member.roles)}```", inline=True)

        embed.add_field(name="Nickname (AKA)", value=f"```{member.nick}```", inline=True)
        embed.add_field(name="Bot?", value="```{}```".format("Yes" if member.bot else "No"), inline=True)
        embed.add_field(name="Top Role", value=f"{member.top_role.mention}", inline=True)

        embed.add_field(name=f"Created At", value="```{}```".format(member.created_at.strftime("%a, %#d %B %Y, %I:%M %p, UTC")), inline=True)
        embed.add_field(name=f"Joined At", value="```{}```".format(member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p, UTC")), inline=True)
        embed.add_field(name="ID", value=f"```{member.id}```", inline=True)

        return await inter.response.send_message(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Profile(bot))
