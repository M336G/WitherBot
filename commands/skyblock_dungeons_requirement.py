from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "skyblock_dungeons_requirement", description= "Show the Catacombs Level Requirements in SkyBlock")
    async def skyblockDungeonsRequirementsCommand(interaction: Interaction):
        embed = Embed(title="Dungeon Levels Requirement",description="")
        embed.add_field(name="\n<:f0:1040298722103398440> Entrance", value="\nCombat Level 15", inline=False)
        embed.add_field(name="\n<:f1:1040298723667890277> Floor 1", value="\nCatacombs Level 1", inline=False)
        embed.add_field(name="\n<:f2:1040298724968120390> Floor 2", value="\nCatacombs Level 3", inline=False)
        embed.add_field(name="\n<:f3:1040298726209638500> Floor 3", value="\nCatacombs Level 5", inline=False)
        embed.add_field(name="\n<:f4:1040298727551803433> Floor 4", value="\nCatacombs Level 9", inline=False)
        embed.add_field(name="\n<:f5:1040298729309229136> Floor 5", value="\nCatacombs Level 14", inline=False)
        embed.add_field(name="\n<:f6:1040298730080968765> Floor 6", value="\nCatacombs Level 19", inline=False)
        embed.add_field(name="\n<:f7:1040298731867734079> Floor 7", value="\nCatacombs Level 24", inline=False)
        embed.add_field(name="\n<:low_master_floor:1040298735047016559> Master Mode Floor 1", value="\nCatacombs Level 24", inline=False)
        embed.add_field(name="\n<:low_master_floor:1040298735047016559> Master Mode Floor 2", value="\nCatacombs Level 26", inline=False)
        embed.add_field(name="\n<:low_master_floor:1040298735047016559> Master Mode Floor 3", value="\nCatacombs Level 28", inline=False)
        embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 4", value="\nCatacombs Level 30", inline=False)
        embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 5", value="\nCatacombs Level 32", inline=False)
        embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 6", value="\nCatacombs Level 34", inline=False)
        embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 7", value="\nCatacombs Level 36", inline=False)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_dungeons_requirement")
