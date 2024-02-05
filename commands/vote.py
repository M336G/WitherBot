from discord import Interaction, Embed, Member, Role, ButtonStyle
from discord.ui import Button, View
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name="vote",description="Vote for the bot on top.gg!")
    async def voteCommand(interaction: Interaction):
        embed = Embed(title=" ",description="**Click the button below to vote for the bot on top.gg!**")
        button = Button(label='Vote for the bot on top.gg!', style=ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
        view = View()
        view.add_item(button)
        await interaction.response.send_message(" ",embed=embed, view=view)
