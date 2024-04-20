from discord import Interaction, Embed, ButtonStyle
from discord.app_commands import allowed_contexts, allowed_installs
from discord.ui import Button, View
from util.functions import log
from datetime import datetime

def commandFunction(tree, client):
    @tree.command(name="credits",description="Show the credits of the bot")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def creditsCommand(interaction: Interaction):
        embed = Embed(title="Credits",description=f" ",colour=8359053)
        embed.add_field(name=" ", value="**<@1039238934682665030> has been created by <@629711559899217950>**", inline=False)
        embed.add_field(name="Special Thanks", value="Special thanks to <@795048346955677748> for giving me the idea to create the bot and <@589349861493833751> for helping me optimize the code!", inline=False)
        embed.add_field(name="Thanks", value="Thanks to <@793225807874883584> and <@472042883763929098> for helping me fixing bugs!", inline=False)

        view = View()

        button = Button(label='Vote for the bot on top.gg', style=ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
        view.add_item(button)
        button = Button(label='Invite the bot on your server', style=ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
        view.add_item(button)

        embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}")
        embed.timestamp = datetime.now()

        await interaction.response.send_message(" ",embed=embed, view=view, ephemeral=False)

        log(f"(SUCCESS) {interaction.user} used /credits")