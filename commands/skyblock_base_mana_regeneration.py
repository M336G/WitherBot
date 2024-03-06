from discord import Interaction, Embed
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "skyblock_base_mana_regeneration", description= "Calculate your Base Mana Regeneration in SkyBlock")
    async def skyblockBaseManaRegenerationCommand(interaction: Interaction, mana: int):
        base_mana_regeneration = mana * 0.02
        embed = Embed(title=" ",description=f"**Your Mana Regeneration rate is {base_mana_regeneration} ✎ Mana/s** ({mana} ✎ Mana)", colour=3447003)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_base_mana_regeneration")