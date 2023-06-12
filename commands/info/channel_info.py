import nextcord
from nextcord import Interaction, Guild
from nextcord import Embed, Color
from nextcord import TextChannel, ForumChannel, VoiceChannel, StageChannel, CategoryChannel
from nextcord.ext.commands import Cog
from typing import Union
from utils.bot import Bot


class ChannelInfo(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Provides information about the current or a given channel")
    async def channel_info(self, inter: Interaction, channel: Union[TextChannel, ForumChannel, VoiceChannel, StageChannel, CategoryChannel] = None):
        channel = inter.channel if not channel else channel
        
        embed = Embed(colour=Color.from_rgb(18, 122, 160))
        self.add_embed_fields_default(channel, embed)

        if isinstance(channel, TextChannel):
            embed.title = "# %s" % channel.name
            self.add_embed_fields_text(channel, embed)
        elif isinstance(channel, ForumChannel):
            embed.title = ":busts_in_silhouette: %s" % channel.name
            self.add_embed_fields_text(channel, embed)
        elif isinstance(channel, VoiceChannel):
            self.add_embed_fields_voice(channel, embed)
        elif isinstance(channel, StageChannel):
            self.add_embed_fields_stage(channel, embed)
        elif isinstance(channel, CategoryChannel):
            self.add_embed_fields_category(channel, embed)

        return await inter.response.send_message(embed=embed)

    def add_embed_fields_default(self, channel: Union[TextChannel, ForumChannel, VoiceChannel, StageChannel, CategoryChannel], embed: Embed):
        create_date = channel.created_at.strftime("%d/%m/%Y")
        jump_url = channel.jump_url
        type = channel.type.__str__().title().replace('_', ' ')
        id = channel.id
        position = channel.position

        embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon.url)

        embed.add_field(name=f"Type", value=f"```{type}```", inline=True)
        embed.add_field(name="Birthdate", value=f"```{create_date}```", inline=True)
        embed.add_field(name="Jump Link", value=f"[Go there]({jump_url})", inline=True)
        
        embed.add_field(name="Position", value=f"```{position}```", inline=True)

        embed.set_footer(text=f"ID: {id}")
    
    def add_embed_fields_text(self, channel: TextChannel, embed: Embed):
        category = channel.category.name if channel.category else "None"
        topic = channel.topic if channel.topic else "None"
        is_nsfw = "Yes" if channel.nsfw else "No"
        members_count = len(channel.members)
        delay = self.get_delay_formatted(channel.slowmode_delay)
 
        embed.add_field(name="Category", value=f"```{category}```", inline=True)
        embed.add_field(name="Topic", value=f"```{topic}```", inline=True)
        
        embed.add_field(name="NSFW?", value=f"```{is_nsfw}```", inline=True)
        embed.add_field(name="Members", value=f"```{members_count}```", inline=True)
        embed.add_field(name="Slowmode Delay", value=f"```{', '.join(delay)}```", inline=True)
    
    def add_embed_fields_voice(self, channel: VoiceChannel, embed: Embed):
        category = channel.category.name if channel.category else "None"
        is_nsfw = "Yes" if channel.nsfw else "No"
        members_in_vc = len(channel.members)
        max_members_in_vc = channel.user_limit if channel.user_limit else "∞"
        bitrate = self.bps_to_kbps(channel.bitrate)
        rtc_region = channel.rtc_region.capitalize() if channel.rtc_region else "Unknown"
        
        embed.title = ":microphone2: %s" % channel.name
        embed.add_field(name="Category", value=f"```{category}```", inline=True)
        embed.add_field(name="Members", value=f"```{members_in_vc} / {max_members_in_vc}```", inline=True)
        
        embed.add_field(name="Bitrate", value=f"```{bitrate}kbps```", inline=True)
        embed.add_field(name="RTC region", value=f"```{rtc_region}```", inline=True)
        embed.add_field(name="NSFW?", value=f"```{is_nsfw}```", inline=True)

    def add_embed_fields_stage(self, channel: StageChannel, embed: Embed):
        category = channel.category.name if channel.category else "None"
        topic = channel.topic if channel.topic else "None"
        bitrate = self.bps_to_kbps(channel.bitrate)
        rtc_region = channel.rtc_region.capitalize() if channel.rtc_region else "Unknown"
        max_members_in_vc = channel.user_limit
        members_in_stage = len(channel.members)
        moderators = len(channel.moderators)
        speakers = len(channel.speakers)
        listeners = len(channel.listeners)

        embed.title = ":satellite: %s" % channel.name
        embed.add_field(name="Category", value=f"```{category}```", inline=True)
        embed.add_field(name="Topic", value=f"```{topic}```", inline=True)
        
        embed.add_field(name=f"Members [{members_in_stage} / {max_members_in_vc}]", value=f"```Moderators: {moderators}\nSpeakers: {speakers}\nListeners: {listeners}```", inline=True)
        embed.add_field(name="Bitrate", value=f"```{bitrate}kbps```", inline=True)
        embed.add_field(name="RTC region", value=f"```{rtc_region}```", inline=True)

    def add_embed_fields_category(self, category: CategoryChannel, embed: Embed):
        all_ch_count = len(category.channels)
        vc_count = len(category.voice_channels)
        text_ch_count = len(category.text_channels)
        others = all_ch_count - (text_ch_count+vc_count)
        is_nsfw = "Yes" if category.nsfw else "No"

        embed.title = ":file_folder: %s" % category.name
        embed.add_field(name=f"Channels [{all_ch_count}]", value=f"```Text: {text_ch_count}\nVoice: {vc_count}\nOthers: {others}```", inline=True)
        embed.add_field(name="NSFW?", value=f"```{is_nsfw}```", inline=True)

    def get_delay_formatted(self, slowmode_delay: int) -> list[str]:
        hours = slowmode_delay // 3600
        slowmode_delay %= 3600
        minutes = slowmode_delay // 60
        slowmode_delay %= 60
        seconds = slowmode_delay

        delay = []
        if hours: delay.append(f"{hours}h")
        if minutes: delay.append(f"{minutes}m")
        if seconds: delay.append(f"{seconds}s")
        if delay == []: delay.append("Off")

        return delay

    def bps_to_kbps(self, bps: int) -> int:
        return bps // 1000


def setup(bot: Bot):
    bot.add_cog(ChannelInfo(bot))
