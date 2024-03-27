from discord import Interaction, Embed
from util.functions import log
from random import randint

def commandFunction(tree, client):
    @tree.command(name= "random_number", description= "Generate a random number")
    async def randomNumberCommand(interaction: Interaction, start: int, stop: int):
        if start == stop:
            embed = Embed(title=" ",description=f":x: **Please use different numbers for the start and stop entries!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            log(f"(FAIL) {interaction.user} FAILED to use /random_number")
            return
        number = randint(start, stop)
        embed = Embed(title=" ",description=f"**Number:** ``{number}``", colour=5763719)
        await interaction.response.send_message(" ",embed=embed) 
        log(f"(SUCCESS) {interaction.user} used /random_number")
