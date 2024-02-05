from discord import Interaction, Embed, Member, Role, ButtonStyle
from discord.ui import Button, View
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name="credits",description="Show the credits of the bot")
    async def creditsCommand(interaction: Interaction):
        embed = Embed(title=" ",description=f"**<@1039238934682665030> has been created by <@629711559899217950>**",colour=8359053)
        
        button = Button(label='Vote for the bot on top.gg', style=ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
        button2 = Button(label='Invite the bot on your server', style=ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
        view = View()
        view.add_item(button)
        view.add_item(button2)

        log(f"(SUCCESS) {interaction.user} used /credits")

        await interaction.response.send_message(" ",embed=embed, view=view, ephemeral=True)