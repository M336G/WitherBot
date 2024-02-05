from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "ping", description="Show the latency between the host and Discord")
    async def ping(interaction: Interaction):
        embed = Embed(title=" ",description=f"<:ping_pong:1039884406552268882> **{round (client.latency * 1000)} ms**", colour=5763719)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} PINGED the bot: {round (client.latency * 1000)} ms")
