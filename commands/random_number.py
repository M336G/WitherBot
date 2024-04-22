from discord import Interaction, Embed
from util.functions import log
from random import randint

def commandFunction(tree, client):
    @tree.command(name= "random_number", description= "Generate a random number/numbers")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def randomNumberCommand(interaction: Interaction, start: int, stop: int, quantity: int = 1):
        if start == stop:
            embed = Embed(title=" ",description=f":x: **Please use different numbers for the start and stop entries!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            log(f"(FAIL) {interaction.user} FAILED to use /random_number")
            return
        if quantity <= 0:
            embed = Embed(title=" ",description=f":x: **Please use numbers that are equal to or bigger than 1!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            log(f"(FAIL) {interaction.user} FAILED to use /random_number")
        elif quantity == 1:
            number = randint(start, stop)
            embed = Embed(title=" ",description=f"**Number:** ``{number}``", colour=5763719)
            await interaction.response.send_message(" ",embed=embed) 
            log(f"(SUCCESS) {interaction.user} used /random_number")
        else:
            numbers = []
            for i in range(quantity):
                i = randint(start, stop)
                numbers.append(i)
            embed = Embed(title=" ",description=f"**Numbers:** ``{numbers}``", colour=5763719)
            await interaction.response.send_message(" ",embed=embed) 
            log(f"(SUCCESS) {interaction.user} used /random_number")
