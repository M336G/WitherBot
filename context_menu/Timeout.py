from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions
from util.functions import log, logUser
from modals.timeout import timeout_form

def commandFunction(tree, client):
    @tree.context_menu(name="Timeout")
    @default_permissions(moderate_members=True)
    async def show_stats(interaction:Interaction, user:Member):
        logUser(interaction.user.id)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description=f":x: **You cannot mute yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to MUTE himself")
        elif 1039238934682665030 == user.id:
            embed = Embed(title=" ",description=f":x: **You cannot mute me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to MUTE the bot")
        else:
            await interaction.response.send_modal(timeout_form(user))
