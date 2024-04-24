from discord import Interaction
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name= "hello", description= "Hello!")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def helloCommand(interaction: Interaction):
        logUser(interaction.user.id)
        await interaction.response.send_message(f"Hello <@{interaction.user.id}>!")

        log(f"(SUCCESS) {interaction.user} used /hello")