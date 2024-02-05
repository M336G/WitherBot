from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "skyblock_damage_reduction", description= "Calculate your Damage Reduction percentage in SkyBlock")
    async def skyblockDamageReductionCommand(interaction: Interaction, defense: int):
        damage_reduction = round(defense/(defense+100)*100,2)
        embed = Embed(title=" ",description=f"**Your Damage Reduction percentage is {damage_reduction}%** ({defense} ❈ Defense)", colour=2067276)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_damage_reduction")