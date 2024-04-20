from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log
from util.resources import ITEMS
from random import randint

def commandFunction(tree, client):
    @tree.command(name= "minecraft_random_item", description= "Choose a random item in Minecraft (1.17.1)")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def minecraftRandomItemCommand(interaction: Interaction):
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
        
        log(f"(SUCCESS) {interaction.user} used /minecraft_random_item")
