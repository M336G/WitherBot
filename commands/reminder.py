from discord import Interaction, Embed
from util.functions import log
from asyncio import sleep as s

def commandFunction(tree, client):
    @tree.command(name= "reminder", description= "Make a reminder for yourself")
    async def reminderCommand(interaction: Interaction, reminder: str = None, days:int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
        time = days + hours + minutes + seconds
        if reminder == None:
            embed = Embed(title=" ",description=f"Please indicate what you want to be reminded of", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            log(f"(FAIL) {interaction.user} FAILED to use /reminder")
            return
        else:
            asyncio.s(time)
            embed = Embed(title=" ",description=f"**I remind you of ``{reminder}``**", colour=5763719)
            await interaction.user.send(" ", embed=embed)
            log(f"(SUCCESS) {interaction.user} used /reminder") 
