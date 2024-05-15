from discord import Interaction, Embed
from discord.app_commands import Group, AppInstallationType, AppCommandContext
from util.functions import log, logUser
from util.resources import BLOCKS, ITEMS
from random import randint

def commandFunction(tree, client):
    group = Group(
        name="random", 
        description="Various commands related to randomization",
        allowed_installs = AppInstallationType(guild=True, user= True),
        allowed_contexts = AppCommandContext(guild=True, dm_channel=True, private_channel=True)
    )
    
    @group.command(name= "block", description= "Choose a random block in Minecraft (up to 1.17.1)")
    async def minecraftRandomBlockCommand(interaction: Interaction):
        logUser(interaction.user.id)
        random_block = BLOCKS[randint(0,len(BLOCKS) - 1)]
        i = 0
        block_list = random_block.split("_")
        random_block = ""
        while(i < len(block_list)):
            block_item = block_list[i]
            block_item = block_item.replace(block_item[0], block_item[0].upper(), 1)
            random_block = f'{random_block} {block_item}'
            i = i + 1
        random_block = random_block.replace(" ", "", 1)
        embed = Embed(title=" ",description=f"**{random_block}**")
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /random block")

    @group.command(name= "item", description= "Choose a random item in Minecraft (up to 1.17.1)")
    async def minecraftRandomItemCommand(interaction: Interaction):
        logUser(interaction.user.id)
        random_item = ITEMS[randint(0,len(ITEMS) - 1)]
        i = 0
        item_list = random_item.split("_")
        random_item = ""
        while(i < len(item_list)):
            item_item = item_list[i]
            item_item = item_item.replace(item_item[0], item_item[0].upper(), 1)
            random_item = f'{random_item} {item_item}'
            i = i + 1
        random_item = random_item.replace(" ", "", 1)
        embed = Embed(title=" ",description=f"**{random_item}**")
        await interaction.response.send_message(" ",embed=embed)
        
        log(f"(SUCCESS) {interaction.user} used /random item")

    @group.command(name= "number", description= "Generate a random number")
    async def randomNumberCommand(interaction: Interaction, start: int, stop: int):
        logUser(interaction.user.id)
        if start == stop:
            embed = Embed(title=" ",description=f":x: **Please use different numbers for the start and stop entries!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            log(f"(FAIL) {interaction.user} FAILED to use /random_number")
            return
        number = randint(start, stop)
        embed = Embed(title=" ",description=f"**Number:** ``{number}``")
        await interaction.response.send_message(" ",embed=embed) 
        log(f"(SUCCESS) {interaction.user} used /random_number")

    tree.add_command(group)