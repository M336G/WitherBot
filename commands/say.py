from discord import Interaction, Embed
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "say", description= "Say something")
    @default_permissions(administrator = True)
    async def sayCommand(interaction: Interaction, message: str):
        embed = Embed(title=" ",description=f"**Message sent in <#{interaction.channel.id}>**", colour=5763719)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        await interaction.channel.send(message)
        
        log(f"(SUCCESS) {interaction.user} used /say on {interaction.user.guild} ({interaction.user.guild.id})")

