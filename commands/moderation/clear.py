import nextcord
from nextcord import Interaction
from nextcord import Embed, Color
from nextcord.ext.commands import Cog, Bot


class Clear(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(description="Deletes a specific number of messages in a given text channel.")
    async def clear(self, inter: Interaction, amount: int = None):
        if not inter.user.guild_permissions.manage_messages:
            return await inter.response.send_message("You don't have 'manage_messages' permission!")
                
        if amount == None:
            amount = 1
        elif amount == 0:
            error = Embed(title="Nothing Was Deleted!", color=Color.from_rgb(14, 39, 46))
            return await inter.response.send_message(embed=error, delete_after=3)
        elif amount < 0:
            amount = abs(amount)

        if amount > 50:
            error = Embed(title="Error :red_circle:",
                description=f"The amount must be a number under or equal to ***50***\n**Your Amount:** ***{amount}***",
                color=Color.red())
            return await inter.response.send_message(embed=error, delete_after=3)

        await inter.channel.purge(limit=amount)
        
        embed = Embed(
            title="Done :green_circle: ",
            description="You deleted ***{}*** {} in this channel.".format(amount, "**messages**" if amount >= 2 else "**message**"),
            color=Color.dark_green()
        )

        return await inter.response.send_message(embed=embed, delete_after=3)


def setup(bot: Bot):
    bot.add_cog(Clear(bot))
