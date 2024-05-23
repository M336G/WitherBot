from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log, logUser, permissionCheck
from datetime import timedelta

def commandFunction(tree, client):
    @tree.command(name= "timeout", description= "Mute someone on your Discord server")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(moderate_members = True)
    async def timeoutCommand(interaction: Interaction, user:Member, reason: str = None, days:int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
        logUser(interaction.user.id)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description=f":x: **You cannot mute yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            

            log(f"(FAIL) {interaction.user} tried to MUTE themselves on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        if 1039238934682665030 == user.id:
            embed = Embed(title=" ",description=f":x: **You cannot mute me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to MUTE the bot on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        if await permissionCheck(user, interaction, ":x: **You cannot mute that user!**", f"(FAIL) {interaction.user} tried to MUTE an admin/user with higher privileges ({user.id}) on {interaction.user.guild} ({interaction.user.guild.id})"):
            return
        time = days + hours + minutes + seconds
        if time == 0:
            days = 7
        timedeltaTimeout = timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        await interaction.response.defer()
        try:
            await user.timeout(timedeltaTimeout,reason=reason)
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{user.id}> **for {days}d {hours}h {minutes}m {seconds}s**{f'\n``Reason: {reason}``' if reason != None else ''}", colour=2067276)
            await interaction.followup.send(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} MUTED {user} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id}){' and gave a reason' if reason != None else ''}")
            try:
                embed = Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**{f'\n``Reason: {reason}``' if reason != None else ''}",description="", colour=15548997)
                await user.send(" ",embed=embed)
            except:
                embed = Embed(title=" ",description=":x: Unable to send to user", colour=15548997)
                await interaction.channel.send(" ",embed=embed)
        except:
            embed = Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
            await interaction.followup.send(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use the /timeout command")
