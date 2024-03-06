from discord import Interaction, Embed
from util.functions import log
from util.resources import BLOCKS
from random import randint

def commandFunction(tree, client):
    @tree.command(name= "minecraft_random_block", description= "Choose a random block in Minecraft (1.17.1)")
    async def minecraftRandomBlockCommand(interaction: Interaction):
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

        log(f"(SUCCESS) {interaction.user} used /minecraft_random_block")
