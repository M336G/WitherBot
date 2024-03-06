from discord import Interaction, Embed, ButtonStyle
from discord.ui import Button, View

def commandFunction(tree, client):
    @tree.command(name="invite",description="Invite the bot on your server!")
    async def inviteCommand(interaction: Interaction):
        embed = Embed(title=" ",description="**Click the button below to add the bot to your server!**")
        button = Button(label='Invite the bot on your server!', style=ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
        view = View()
        view.add_item(button)
        await interaction.response.send_message(" ",embed=embed, view=view)