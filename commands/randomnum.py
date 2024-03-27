from discord import Interaction, Embed
from util.functions import log
from random import randint

def commandFunction(tree, client):
    @tree.command(name= "randomnum", description= "generating random number")
    async def randomnumCommand(interaction: Interaction, from1: int, to: int):
        if from1 == None or to == None:
            embed = Embed(title=" ",description=f"Please specify from which number and to which number you want to generate", colour=5763719)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        else:
            num1 = random.randint(from1, to)
            embed = Embed(title=" ",description=f"**Your random number is: {num1}. Nice!**", colour=5763719)
            await interaction.response.send_message(" ",embed=embed) 
        
        log(f"(SUCCESS) {interaction.user} used /randomnum")
