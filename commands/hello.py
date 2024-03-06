from discord import Interaction
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "hello", description= "Hello!")
    async def helloCommand(interaction: Interaction):
        await interaction.response.send_message(f"Hello <@{interaction.user.id}>!")

        log(f"(SUCCESS) {interaction.user} used /hello")