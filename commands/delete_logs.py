from discord import Interaction, Embed
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from datetime import date, datetime

def commandFunction(tree, client):
    @tree.command(name="delete_logs",description="A command used by M336 to clear the logs")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(administrator=True)
    async def deleteLogsCommand(interaction: Interaction):
        if interaction.user.id != 629711559899217950:
            embed = Embed(title=" ",description="**:x: You cannot use this command!**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        elif interaction.guild.id != 1191505948959842344:
            embed = Embed(title=" ",description="**:x: You cannot use this command here!**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        else:
            try:
                f = open("logs.txt", "w")
                f.write(f"[{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M:%S')}] (RESET) Logs have been RESET\n")
                f.close()
                embed = Embed(title=" ",description="**Logs have been reset!**",colour=2067276)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            except:
                embed = Embed(title=" ",description="**:x: An error has occured while trying to reset the logs**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)