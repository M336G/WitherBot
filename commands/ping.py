from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "ping", description="Show the latency between the host and Discord")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ping(interaction: Interaction):
        embed = Embed(title=" ",description=f"<:ping_pong:1039884406552268882> **{round (client.latency * 1000)} ms**", colour=2067276)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} PINGED the bot: {round (client.latency * 1000)} ms")