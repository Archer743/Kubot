import nextcord
import os
from nextcord import Interaction
from nextcord import Embed, Color
from nextcord import TextChannel, Message
from nextcord.ext.commands import Cog, Bot


class DownloadChannelFiles(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Downloads all files in a text channel.")
    async def download_channel_files(self, inter: Interaction, channel: TextChannel, path: str):
        if inter.user.id != self.bot.owner:
            return await inter.response.send_message("You are not my owner so you can't use this command!")
        
        if not os.path.exists(path):
            return await inter.response.send_message("Path doesn't exist!")

        response = await inter.send(f"Starting...")
        messages = [message async for message in channel.history(limit=None)]
        await response.edit(f"All messages were fetched. Files will be downloaded soon (trust)")
        cur_filename_id = 1

        for message in messages:
            for attachment in message.attachments:
                file_extention = attachment.filename.split('.').pop()
                full_path = os.path.join(path, f"{cur_filename_id}.{file_extention}") 
                await attachment.save(full_path)
                cur_filename_id += 1
        
        final_msg = f"Done! **{cur_filename_id-1}** files were saved in ``{path}``" if cur_filename_id != 1 else f"No files found in {channel.mention}!"

        await response.edit(final_msg)

        # counter = len([message async for message in channel.history(limit=None)])
        # await response.edit(f"Done! {counter} messages")


def setup(bot: Bot):
    bot.add_cog(DownloadChannelFiles(bot))
