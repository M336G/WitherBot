from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log, logUser, permissionCheck

def commandFunction(tree, client):    
    @tree.command(name= "kick", description= "Kick someone from your Discord server")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(kick_members = True)
    async def kickCommand(interaction: Interaction, user: Member, reason:str = None):
        logUser(interaction.user.id)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to KICK themselves on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        if 1039238934682665030 == user.id:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to KICK the bot on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        if permissionCheck(user, interaction, ":x: **You cannot kick this user!**", f"(FAIL) {interaction.user} tried to KICK an admin/user with higher privileges ({user.id}) on {interaction.user.guild} ({interaction.user.guild.id})"):
            return
        try:
            await interaction.response.defer()
            await user.kick(reason=reason)
            try:
                embed = Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**{f'\n``Reason: {reason}``' if reason != None else ''}",description="", colour=15548997)
                await user.send(" ",embed=embed)
            except:
                await interaction.channel.send(" ",embed=Embed(description=f":x: Unable to send to user", colour=15548997))
            embed = Embed(title=" ",description=f"**``{user}`` has been kicked from the server!**{f'\n**``Reason: {reason}``**' if reason != None else ''}", colour=2067276)
            await interaction.followup.send(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} has KICKED {user} on {interaction.user.guild} ({interaction.user.guild.id}){' and gave a reason' if reason != None else ''}")
        except:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.followup.send(" ",embed=embed)

            log(f"(FAIL) {interaction.user} has failed using the /kick command")
