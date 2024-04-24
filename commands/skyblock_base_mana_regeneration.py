from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name= "skyblock_base_mana_regeneration", description= "Calculate your Base Mana Regeneration in SkyBlock")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def skyblockBaseManaRegenerationCommand(interaction: Interaction, mana: int):
        logUser(interaction.user.id)
        base_mana_regeneration = mana * 0.02
        embed = Embed(title=" ",description=f"**Your Mana Regeneration rate is {base_mana_regeneration} ✎ Mana/s** ({mana} ✎ Mana)", colour=3447003)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_base_mana_regeneration")