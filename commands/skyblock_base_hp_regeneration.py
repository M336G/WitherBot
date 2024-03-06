from discord import Interaction, Embed
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "skyblock_base_hp_regeneration", description= "Calculate your Base Health Regeneration in SkyBlock")
    async def skyblockBaseHpRegenerationCommand(interaction: Interaction, health: int):
        base_health_regeneration = ((health*0.01)+1.5)
        embed = Embed(title=" ",description=f"**Your Health Regeneration rate is {base_health_regeneration} ❤ Health/s** ({health} ❤ Health)", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_base_hp_regeneration")
