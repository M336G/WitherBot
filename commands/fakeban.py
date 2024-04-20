from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "fakeban", description= "Fakeban someone on your Discord server")
    @allowed_installs(guilds=True, users=False)
    @allowed_contexts(guilds=True, dms=False, private_channels=True)
    @default_permissions(ban_members = True)
    async def fakeBanCommand(interaction: Interaction, user: Member, reason:str = None):
        if reason == None:
            embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**", colour=2067276)
            await interaction.response.send_message(" ",embed=embed)
            embed = Embed(title=" ",description=f"**You have been <:gregban:1039247298808520794> fakebanned from ``{interaction.guild.name}``.**")
            await user.send(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} has FAKEBANNED {user} on {interaction.user.guild} ({interaction.user.guild.id})")
        else:
            embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**\n**``Reason: {reason}``**", colour=2067276)
            await interaction.response.send_message(" ",embed=embed)
            embed = Embed(title=" ",description=f"**You have been <:gregban:1039247298808520794> fakebanned from ``{interaction.guild.name}``\n**``Reason: {reason}``**.**")
            await user.send(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} has FAKEBANNED {user} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
