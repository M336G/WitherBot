from discord import Interaction, Embed
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "youtube", description= "Watch YouTube Together")
    async def youtubeCommand(interaction: Interaction):
        try:
            link = await tree.togetherControl.create_link(interaction.user.voice.channel.id, 'youtube')
            embed = Embed(title="Watch Together: YouTube",description=f"Click the link below to start the activity\n{link}", colour=2067276)
            await interaction.response.send_message(" ", embed=embed)

            log(f"(SUCCESS) {interaction.user} started an activity (YouTube Together) on {interaction.user.guild} ({interaction.user.guild.id})")
        except:
            embed = Embed(title=" ",description=":x: **An error occurred. Are you in a voice channel?**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use the /youtube command")
