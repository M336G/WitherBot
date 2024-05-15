from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log, logUser, permissionCheck

def commandFunction(tree, client):
    @tree.command(name= "ban", description= "Ban someone on your Discord server")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(ban_members = True)
    async def banCommand(interaction: Interaction, user: Member, reason:str = None):
        logUser(interaction.user.id)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to BAN himself on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        if 1039238934682665030 == user.id:
            embed = Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to BAN the bot on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        if await permissionCheck(user, interaction, ":x: **You cannot ban this user!**", f"(FAIL) {interaction.user} tried to BAN an admin/user with higher privileges ({user.id}) on {interaction.user.guild} ({interaction.user.guild.id})"):
            return
        try:
            await interaction.response.defer()
            await user.ban(reason=reason)
            try:
                embed = Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**{f'\n``Reason: {reason}``' if reason != None else ''}",description="", colour=15548997)
                await user.send(" ",embed=embed)
            except:
                await interaction.channel.send(" ",embed=Embed(description=f":x: Unable to send to user", colour=15548997))
            embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**{f'\n**``Reason: {reason}``**' if reason != None else ''}", colour=2067276)
            await interaction.followup.send(" ",embed=embed)
            log(f"(SUCCESS) {interaction.user} has BANNED {user} on {interaction.user.guild} ({interaction.user.guild.id}){' and gave a reason' if reason != None else ''}")
        except:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.followup.send(" ",embed=embed)

            log(f"(FAIL) {interaction.user} has failed using the /ban command")
