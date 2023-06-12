import nextcord
from nextcord import Interaction, Guild, ChannelType
from nextcord import Embed, Color
from nextcord.ext.commands import Cog
from utils.bot import Bot


class ServerInfo(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Provides information about the current server")
    async def server_info(self, inter: Interaction):
        # Information
        guild = inter.guild

        guild_name = guild.name
        guild_id = guild.id
        owner = guild.owner if guild.owner else "None"
        create_date = guild.created_at.strftime("%d/%m/%Y")
        verify_level = guild.verification_level.__str__().title()

        members_count = guild.member_count
        bots_count = len(guild.bots)
        real_users_count = members_count - bots_count
        
        role_count = len(guild.roles)
        highest_role = guild.roles[-1]

        emoji_count = len(guild.emojis)
        emoji_limit = guild.emoji_limit

        all_ch = len(guild.channels)
        text_ch = len(guild.text_channels)
        voice_ch = len(guild.voice_channels)
        scheduled_events = len(guild.scheduled_events)

        # Embed
        embed = Embed(title="%s" % guild_name,
                      colour=Color.from_rgb(18, 122, 160))

        embed.add_field(name="Owner", value=f"{owner.mention}", inline=True)
        embed.add_field(name="Birthdate", value=f"```{create_date}```", inline=True)
        embed.add_field(name="Verification", value=f"```{verify_level}```", inline=True)

        embed.add_field(name="Highest Role", value=f"{highest_role.mention}", inline=True)
        embed.add_field(name="Roles", value=f"```{role_count}```", inline=True)
        embed.add_field(name="Emojies", value=f"```{emoji_count} / {emoji_limit}```", inline=True)

        embed.add_field(name=f"Channels [{all_ch}]", value=f"```Text: {text_ch}\nVoice: {voice_ch}\nOthers: {all_ch-(text_ch+voice_ch)}```", inline=True)
        embed.add_field(name=f"Members [{members_count}]", value=f"```Users: {real_users_count}\nBots: {bots_count}```", inline=True)
        embed.add_field(name="Scheduled events", value=f"```{scheduled_events}```", inline=True)

        embed.set_thumbnail(guild.icon.url)
        embed.set_footer(text=f"ID: {guild_id}")
        
        return await inter.response.send_message(embed=embed)


def setup(bot: Bot):
    bot.add_cog(ServerInfo(bot))
