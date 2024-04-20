from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "skyblock_ehp", description= "Calculate your EHP in SkyBlock")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def skyblockEhpCommand(interaction: Interaction, health: int, defense: int):
        ehp = health*(1+defense/100)
        embed = Embed(title=" ",description=f"**Your EHP is {ehp}** ({health} ❤ Health and {defense} ❈ Defense)", colour=2067276)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_ehp")