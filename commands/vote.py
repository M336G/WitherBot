from discord import Interaction, Embed, ButtonStyle
from discord.app_commands import allowed_contexts, allowed_installs
from discord.ui import Button, View
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name="vote",description="Vote for the bot on top.gg!")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def voteCommand(interaction: Interaction):
        logUser(interaction.user.id)
        embed = Embed(title=" ",description="**Click the button below to vote for the bot on top.gg!**")
        button = Button(label='Vote for the bot on top.gg!', style=ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
        view = View()
        view.add_item(button)
        await interaction.response.send_message(" ",embed=embed, view=view)
        log(f"(SUCCESS) {interaction.user} used /vote")