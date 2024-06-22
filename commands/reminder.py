from discord import Interaction, Embed
from discord.app_commands import Group, AppInstallationType, AppCommandContext
from util.functions import log, logUser
import asyncio

def commandFunction(tree, client):
    @tree.command(name= "reminder", description= "Make a reminder for yourself any time")
    async def reminderCommand(interaction: Interaction, time, text):
        time = int(time)
        if time == 0:
            embed = Embed(title=" ",description=f":x: **Please, choose any time what bigger than 0**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)  
            log(f"(FAIL) {interaction.user} failed to use the /reminder command")
        if not text:
            embed = Embed(title=" ",description=f":x: **Please, write text**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True) 
            log(f"(FAIL) {interaction.user} failed to use the /reminder command")
        else:
            embed = Embed(title=" ",description=f":x: **The text will be sent in: {time} seconds **", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            await asyncio.sleep(time)
            embed = Embed(title="Reminder",description=f" {text}", colour=15548997)
            await interaction.user.send(" ", embed=embed)
            log(f"(SUCCESS) {interaction.user} used command /reminder")
