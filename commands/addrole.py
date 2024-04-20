from discord import Interaction, Embed, Member, Role, app_commands
from util.functions import log

def commandFunction(tree:app_commands.CommandTree, client):
    @tree.command(name= "addrole", description= "Add a role to someone on your Discord server")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
    @app_commands.default_permissions(manage_roles = True)
    async def addRoleCommand(interaction: Interaction, member: Member, role: Role):
        try:
            await member.add_roles(role)
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully added** ``{role}`` **to** ``{member}``**.**",colour=5763719)
            await interaction.response.send_message(" ",embed=embed)
            
            log(f"(SUCCESS) {interaction.user} ADDED a role to {member} on {interaction.user.guild} ({interaction.user.guild.id})")

        except:
            embed = Embed(title=" ",description=f":x: **An error occured**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use /addrole")
