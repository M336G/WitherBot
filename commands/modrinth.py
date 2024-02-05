from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log
from requests import get as requestGet
from datetime import datetime

def commandFunction(tree, client):    
    @tree.command(name="modrinth",description="Search a project on Modrinth with its ID or its slug")
    async def modrinthCommand(interaction: Interaction, query: str):
        try:
            res = requestGet(
                url="https://api.modrinth.com/v2/project/"+query
            ).json()

            embed = Embed(title=f'{res["title"]}',description=f'> **{res["description"]}**\n\n**Type:** ``{res["project_type"]}``\n**Project ID:** ``{res["id"]}``\n**Project Slug:** ``{res["slug"]}``\n**License:** ``{res["license"]["id"]}``\n\n**Client compatibility:** ``{res["client_side"]}``\n**Server compatibility:** ``{res["server_side"]}``\n\n**Downloads:** ``{res["downloads"]}``\n**Followers** ``{res["followers"]}``\n\n',colour=2067276)
            embed.set_thumbnail(url=res["icon_url"])
            embed.set_footer(text=f"Wither Bot", icon_url="https://static.wikia.nocookie.net/minecraft_fr_gamepedia/images/a/aa/Wither.png")
            embed.timestamp = datetime.now()
            await interaction.response.send_message(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} used /modrinth")

        except:
            embed = Embed(title=" ",description=":x: **Couldn't find the project. Have you entered the project's slug or ID correctly?**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)

            log(f"(FAIL) {interaction.user} failed to use the /modrinth command (Invalid project's slug or ID?)")
