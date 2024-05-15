from discord import Interaction, Embed, Member, Role, Permissions
from discord.app_commands import Group, AppInstallationType, AppCommandContext, default_permissions
from util.functions import log, logUser, permissionCheck

def commandFunction(tree, client):
    group = Group(
        name="role", 
        description="Add or remove a role from someone",
        allowed_installs = AppInstallationType(guild=True, user= False),
        allowed_contexts = AppCommandContext(guild=True, dm_channel=False, private_channel=False),
        default_permissions= Permissions(manage_roles = True)
    )

    @group.command(name= "add", description= "Add a role to someone on your server")
    async def addRoleCommand(interaction: Interaction, member: Member, role: Role):
        logUser(interaction.user.id)
        if role in member.roles:
            await interaction.response.send_message(embed=Embed(description=":x: **This user does already have that role!**", colour=15548997))
            return
        if await permissionCheck(role, interaction, ":x: **You cannot add this role!**", f"(FAIL) {interaction.user} tried to add a role with higher privileges ({role.id}) on {interaction.user.guild} ({interaction.user.guild.id})"):
            return
        try:
            await member.add_roles(role)
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully added** ``{role}`` **to** ``{member}``**.**",colour=2067276)
            await interaction.response.send_message(" ",embed=embed)
            log(f"(SUCCESS) {interaction.user} ADDED a role to {member} on {interaction.user.guild} ({interaction.user.guild.id})")

        except:
            embed = Embed(title=" ",description=f":x: **An error occured**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            log(f"(FAIL) {interaction.user} failed to use /addrole")

    @group.command(name= "remove", description= "Remove a role from someone on your Discord server")
    async def removeRoleCommand(interaction: Interaction, member: Member, role: Role):
        logUser(interaction.user.id)
        if not role in member.roles:
            await interaction.response.send_message(embed=Embed(description=":x: **This user does not have that role!**", colour=15548997))
            return
        if await permissionCheck(role, interaction, ":x: **You cannot remove this role!**", f"(FAIL) {interaction.user} tried to remove a role with higher privileges ({role.id}) on {interaction.user.guild} ({interaction.user.guild.id})"):
            return
        try:
            await member.remove_roles(role)
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully removed** ``{role}`` **from** ``{member}``**.**",colour=2067276)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} REMOVED a role from {member} on {interaction.user.guild} ({interaction.user.guild.id})")
        except:
            embed = Embed(title=" ",description=f":x: **An error occured**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use /removerole")

    tree.add_command(group)