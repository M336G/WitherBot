from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "ban", description= "Ban someone on your Discord server")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(ban_members = True)
    async def banCommand(interaction: Interaction, user: Member, reason:str = None):
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to BAN himself on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        elif 1039238934682665030 == user.id:
            embed = Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to BAN the bot on {interaction.user.guild} ({interaction.user.guild.id})")
            return
        else:
            try:
                if reason == None:
                    try:
                        embed = Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**",description="", colour=15548997)
                        await user.send(" ",embed=embed)
                    except:
                        embed2 = Embed(title="")
                    await user.ban(reason=reason)
                    embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**", colour=2067276)
                    await interaction.response.send_message(" ",embed=embed)
                    await interaction.channel.send(" ",embed=embed2)

                    log(f"(SUCCESS) {interaction.user} has BANNED {user} on {interaction.user.guild} ({interaction.user.guild.id})")
                    
                else:
                    try:
                        embed = Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**\n``Reason: {reason}``",description="", colour=15548997)
                        await user.send(" ",embed=embed)
                    except:
                        embed2 = Embed(title="")
                    await user.ban(reason=reason)
                    embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**\n**``Reason: {reason}``**", colour=2067276)
                    await interaction.response.send_message(" ",embed=embed)
                    await interaction.channel.send(" ",embed=embed2)

                    log(f"(SUCCESS) {interaction.user} has BANNED {user} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
            except:
                embed = Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
                await interaction.response.send_message(" ",embed=embed)

                log(f"(FAIL) {interaction.user} has failed using the /ban command")
