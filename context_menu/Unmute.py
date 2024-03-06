from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions
from util.functions import log
from datetime import timedelta

def commandFunction(tree, client):
    @tree.context_menu(name="Unmute")
    @default_permissions(moderate_members=True)
    async def show_stats(interaction:Interaction, user:Member):
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        timedeltaTimeout = timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        try:
            await user.timeout(timedeltaTimeout, reason="Unmuted")
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully unmuted** <@{user.id}>", colour=5763719)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} UNMUTED {user} on {interaction.user.guild.name} ({interaction.user.guild.id})")
            try:
                embed = Embed(title=f"**You have been unmuted on ``{interaction.guild.name}``**",description="", colour=5763719)
                await user.send(" ",embed=embed)
            except:
                embed = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await interaction.channel.send(" ",embed=embed)
        except:
            embed = Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use the mute application")
