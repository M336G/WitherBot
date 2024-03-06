from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions
from util.functions import log
from datetime import timedelta

def commandFunction(tree, client):
    @tree.command(name= "timeout", description= "Mute someone on your Discord server")
    @default_permissions(moderate_members = True)
    async def timeoutCommand(interaction: Interaction, user:Member, reason: str = None, days:int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
        time = days + hours + minutes + seconds
        if time == 0:
            days = 7
        timedeltaTimeout = timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description=f":x: **You cannot mute yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            

            log(f"(FAIL) {interaction.user} tried to MUTE himself on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        elif 1039238934682665030 == user.id:
            embed = Embed(title=" ",description=f":x: **You cannot mute me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to MUTE the bot on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        try:
            if reason == None:
                await user.timeout(timedeltaTimeout,reason=reason)
                embed = Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{user.id}> **for {days}d {hours}h {minutes}m {seconds}s**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)

                log(f"(SUCCESS) {interaction.user} MUTED {user} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id})")
                try:
                    embed = Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**",description="", colour=15548997)
                    await user.send(" ",embed=embed)
                except:
                    embed = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                    await interaction.channel.send(" ",embed=embed)
            else:
                await user.timeout(timedeltaTimeout,reason=reason)
                embed = Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{user.id}> **for {days}d {hours}h {minutes}m {seconds}s**\n``Reason: {reason}``", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)

                log(f"(SUCCESS) {interaction.user} MUTED {user} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
                try:
                    embed = Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**\n``Reason: {reason}``",description="", colour=15548997)
                    await user.send(" ",embed=embed)
                except:
                    embed = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                    await interaction.channel.send(" ",embed=embed)
        except:
            embed = Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use the /timeout command")
