from discord import Interaction, Embed, ButtonStyle
from discord.app_commands import allowed_contexts, allowed_installs
from discord.ui import Button, View
from util.functions import log, logUser

def commandFunction(tree, client):
    @tree.command(name="invite",description="Invite the bot on your server!")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def inviteCommand(interaction: Interaction):
        logUser(interaction.user.id)
        embed = Embed(title=" ",description="**Click the button below to add the bot to your server!**")
        button = Button(label='Invite the bot on your server!', style=ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
        view = View()
        view.add_item(button)
        await interaction.response.send_message(" ",embed=embed, view=view)
        log(f"(SUCCESS) {interaction.user} used /invite")