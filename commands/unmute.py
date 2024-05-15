from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log, logUser, permissionCheck
from datetime import timedelta

def commandFunction(tree, client):
    @tree.command(name="unmute",description="Unmute someone on your Discord server")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(moderate_members = True)
    async def unmuteCommand(interaction:Interaction, user:Member):
        logUser(interaction.user.id)
        if await permissionCheck(user, interaction, ":x: **You cannot unmute that user!**", f"(FAIL) {interaction.user} tried to UNMUTE an admin/user with higher privileges ({user.id}) on {interaction.user.guild} ({interaction.user.guild.id})"):
            return
        if not user.is_timed_out():
            await interaction.response.send_message(embed=Embed(description=":x: **That user is not muted!**", colour=15548997))
            log(f"(FAIL) {interaction.user} tried to UNMUTE a not muted user on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        timedeltaTimeout = timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        try:
            await user.timeout(timedeltaTimeout, reason="Unmute")
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully unmuted** <@{user.id}>", colour=2067276)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} UNMUTED {user} on {interaction.user.guild} ({interaction.user.guild.id})")
            try:
                embed = Embed(title=f"**You have been unmuted on ``{interaction.guild.name}``**",description="", colour=2067276)
                await user.send(" ",embed=embed)
            except:
                embed = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await interaction.channel.send(" ",embed=embed)
        except:
            embed = Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use the /unmute command")