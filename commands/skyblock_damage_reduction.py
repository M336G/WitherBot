from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name= "skyblock_damage_reduction", description= "Calculate your Damage Reduction percentage in SkyBlock")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def skyblockDamageReductionCommand(interaction: Interaction, defense: int):
        logUser(interaction.user.id)
        damage_reduction = round(defense/(defense+100)*100,2)
        embed = Embed(title=" ",description=f"**Your Damage Reduction percentage is {damage_reduction}%** ({defense} ❈ Defense)", colour=2067276)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_damage_reduction")