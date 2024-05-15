from discord import Interaction, Embed
from discord.app_commands import Group, AppInstallationType, AppCommandContext
from util.functions import log, logUser
from requests import get as requestGet
from random import randint

def commandFunction(tree, client):
    group = Group(
        name="skyblock",
        description="Various SkyBlock util commands",
        allowed_installs = AppInstallationType(guild=True, user= True),
        allowed_contexts = AppCommandContext(guild=True, dm_channel=True, private_channel=True)
    )
    
    @group.command(name= "ehp", description= "Calculate your EHP in SkyBlock")
    async def skyblockEhpCommand(interaction: Interaction, health: int, defense: int):
        logUser(interaction.user.id)
        await interaction.response.send_message(" ",embed=Embed(title=" ",description=f"**Your EHP is {health*(1+defense/100)}** ({health} ❤ Health and {defense} ❈ Defense)", colour=2067276))
        log(f"(SUCCESS) {interaction.user} used /skyblock ehp")

    @group.command(name= "damage_reduction", description= "Calculate your Damage Reduction percentage in SkyBlock")
    async def skyblockDamageReductionCommand(interaction: Interaction, defense: int):
        logUser(interaction.user.id)
        embed = Embed(title=" ",description=f"**Your Damage Reduction percentage is {round(defense/(defense+100)*100,2)}%** ({defense} ❈ Defense)", colour=2067276)
        await interaction.response.send_message(" ",embed=embed)
        log(f"(SUCCESS) {interaction.user} used /skyblock damage_reduction")

    @group.command(name= "regeneration", description= "Calculate your Base Health/Mana Regeneration in SkyBlock")
    async def skyblockBaseHpRegenerationCommand(interaction: Interaction, health: int = 0, mana: int = 0):
        if (health == 0 and mana == 0) or (health != 0 and mana != 0) or (health < 0 or mana < 0):
            await interaction.response.send_message(embed=Embed(description=":x: **Enter one positive value!**",colour=15548997))
            return
        logUser(interaction.user.id)
        base_regeneration = mana * 0.02 if health == 0 else ((health*0.01)+1.5)
        embed = Embed(title=" ",description=f"**Your {'Mana' if health == 0 else 'Health'} Regeneration rate is {base_regeneration} {f'✎ Mana/s** ({mana} ✎ Mana)' if health == 0 else f'❤ Health/s** ({health} ❤ Health)'}", colour=3131390 if health == 0 else 15548997)
        await interaction.response.send_message(" ",embed=embed)
        log(f"(SUCCESS) {interaction.user} used /skyblock regeneration")

    @group.command(name= "dungeons_requirement", description= "Show the Catacombs Level Requirements in SkyBlock")
    async def skyblockDungeonsRequirementsCommand(interaction: Interaction):
        logUser(interaction.user.id)
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
        log(f"(SUCCESS) {interaction.user} used /skyblock dungeons_requirement")
    
    @group.command(name= "randomitem", description="Choose a random SkyBlock item")
    async def skyblockRandomItemCommand(interaction:Interaction):
        await interaction.response.defer()
        logUser(interaction.user.id)
        items = requestGet(
            url="https://api.hypixel.net/resources/skyblock/items"
        ).json()
        ind = randint(1,4103)
        item = str(items["items"][ind]["name"])
        try:
            lore = str(items["items"][ind]["description"])+"\n"
        except:
            lore = ""
        try:
            rarity = str(items["items"][ind]["tier"])
        except:
            rarity = "None"
        embed = Embed(title=" ",description=f"``{item}``\n{lore}**{rarity}**")
        await interaction.followup.send(" ",embed=embed)
        log(f"(SUCCESS) {interaction.user} used /skyblock randomitem")
    
    tree.add_command(group)