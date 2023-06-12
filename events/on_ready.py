from nextcord import Embed, utils
from nextcord.ext.commands import Cog
from datetime import datetime
from utils.bot import Bot


class OnReady(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{now}] {self.bot.user.name} is online!")
        await self.send_ready_message(now)
    
    async def send_ready_message(self, time: str):
        try:
            guild = utils.get(self.bot.guilds, id=int(self.bot.loader.config["HOME_SERVER_ID"]))
            on_ready_channel = utils.get(guild.channels, id=int(self.bot.loader.config["ON_READY_CHANNEL_ID"]))
            avatar_url = self.bot.user.avatar.url if self.bot.user.avatar else self.bot.user.default_avatar.url

            time_split = time.split(sep = ' ')

            msg_embed = Embed(
                title=f"{self.bot.user.name} is back on track!",
                color=self.bot.user.accent_colour
            )

            msg_embed.set_thumbnail(url=avatar_url)
            msg_embed.add_field(name=":calendar_spiral: Date", value=f"```{time_split[0]}```", inline=True)
            msg_embed.add_field(name=":alarm_clock: Time", value=f"```{time_split[1]}```")

            return await on_ready_channel.send(embed=msg_embed)
        except:
            print(f"[{time}] on_ready server message was not sent")


def setup(bot: Bot):
    bot.add_cog(OnReady(bot))