from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name= "skyblock_base_hp_regeneration", description= "Calculate your Base Health Regeneration in SkyBlock")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def skyblockBaseHpRegenerationCommand(interaction: Interaction, health: int):
        logUser(interaction.user.id)
        base_health_regeneration = ((health*0.01)+1.5)
        embed = Embed(title=" ",description=f"**Your Health Regeneration rate is {base_health_regeneration} ❤ Health/s** ({health} ❤ Health)", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_base_hp_regeneration")
