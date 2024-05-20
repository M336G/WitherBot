from discord import Interaction
from discord.app_commands import allowed_contexts, allowed_installs
def commandFunction(tree, client):
    @tree.command(name= "httpcat", description= "Cat")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def catCommand(interaction:Interaction, code:int):
        await interaction.response.send_message(f"https://http.cat/{code}")
