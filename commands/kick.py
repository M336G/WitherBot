from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):    
    @tree.command(name= "kick", description= "Kick someone from your Discord server")
    @default_permissions(kick_members = True)
    async def kickCommand(interaction: Interaction, user: Member, reason:str = None):
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to KICK himself on {interaction.user.guild} ({interaction.user.guild.id})")
        elif 1039238934682665030 == user.id:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to KICK the bot on {interaction.user.guild} ({interaction.user.guild.id})")
        else:
            try:
                if reason == None:
                    try:
                        embed = Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**",description="", colour=15548997)
                        await user.send(" ",embed=embed)
                    except:
                        embed2 = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                    await interaction.channel.send(" ",embed=embed)
                    await user.kick(reason=reason)
                    embed = Embed(title=" ",description=f"**``{user}`` has been kicked from the server!**", colour=5763719)
                    await interaction.response.send_message(" ",embed=embed)
                    await interaction.channel.send(" ",embed=embed2)

                    log(f"(SUCCESS) {interaction.user} has KICKED {user} on {interaction.user.guild} ({interaction.user.guild.id})")
                else:
                    try:
                        embed = Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**\n``Reason: {reason}``",description="", colour=15548997)
                        await user.send(" ",embed=embed)
                    except:
                        embed2 = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                    await user.kick(reason=reason)
                    embed = Embed(title=" ",description=f"**``{user}`` has been kicked from the server!**\n**``Reason: {reason}``**", colour=5763719)
                    await interaction.response.send_message(" ",embed=embed)
                    await interaction.channel.send(" ",embed=embed2)

                    log(f"(SUCCESS) {interaction.user} has KICKED {user} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
            
            except:
                embed = Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
                await interaction.response.send_message(" ",embed=embed)

                log(f"(FAIL) {interaction.user} has failed using the /kick command")