from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions
from util.functions import log, logUser
from modals.kick import kick_form

def commandFunction(tree, client):
    @tree.context_menu(name="Kick")
    @default_permissions(kick_members=True)
    async def show_stats(interaction:Interaction, user:Member):
        logUser(interaction.user.id)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to KICK himself")
        elif 1039238934682665030 == user.id:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to KICK the bot")
        else:
            await interaction.response.send_modal(kick_form(user))
