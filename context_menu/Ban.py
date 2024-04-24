from discord import Interaction, Embed, Member
from discord.app_commands import default_permissions
from util.functions import log, logUser
from modals.ban import ban_form

def commandFunction(tree, client):
    @tree.context_menu(name="Ban")
    @default_permissions(ban_members=True)
    async def show_stats(interaction:Interaction, user:Member):
        logUser(interaction.user.id)
        if interaction.user.id == user.id:
            embed = Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban yourself!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to BAN himself")
        elif 1039238934682665030 == user.id:
            embed = Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban me!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} tried to BAN the bot")
        else:
            await interaction.response.send_modal(ban_form(user))
