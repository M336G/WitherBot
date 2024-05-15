from discord import Interaction, Embed
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name= "say", description= "Say something")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(administrator = True)
    async def sayCommand(interaction: Interaction, message: str):
        logUser(interaction.user.id)
        embed = Embed(title=" ",description=f"**Message sent in <#{interaction.channel.id}>**", colour=2067276)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        await interaction.channel.send(message)
        
        log(f"(SUCCESS) {interaction.user} used /say on {interaction.user.guild} ({interaction.user.guild.id})")