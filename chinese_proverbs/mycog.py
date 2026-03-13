from redbot.core import commands, app_commands
import discord
from .proverbs import run 
class MyCog(commands.Cog):
    """Chinese-Proverbs"""

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="proverb", description="Get a random Chinese proverb")
    async def proverb(self, interaction: discord.Interaction):
        count = 1
        await run(interaction, count)
        

        
