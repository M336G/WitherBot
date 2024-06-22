from discord import Interaction, Embed
from discord.app_commands import Group, AppInstallationType, AppCommandContext
from util.functions import log, logUser

@bot.slash_command(name='reminder', description='test')
async def reminderCommand(interaction: Interaction, time, text):
    time = int(time)
    if time == 0:
        embed = Embed(title=" ",description=f":x: **Please, choose any time what bigger than 0**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)  
    if not text:
        embed = Embed(title=" ",description=f":x: **Please, write text**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True) 
    else:
        embed = Embed(title=" ",description=f":x: **The text will be sent in: {time} seconds **", colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        await asyncio.sleep(time)
        embed = Embed(title="Reminder",description=f":x: {text}", colour=15548997)
        await interaction.user.send(" ", embed=embed)
