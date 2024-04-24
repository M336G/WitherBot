from discord import Interaction, Embed, ButtonStyle
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log, logUser
from requests import get as requestGet
from datetime import datetime
from discord.ui import Button, View

def commandFunction(tree, client):    
    @tree.command(name="modrinth",description="Search a project on Modrinth with its ID or its slug")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def modrinthCommand(interaction: Interaction, query: str):
        logUser(interaction.user.id)
        try:
            res = requestGet(
                url="https://api.modrinth.com/v2/project/"+query
            ).json()
        except:
            embed = Embed(title=" ",description=":x: **Couldn't find the project. Have you entered the project's slug or ID correctly?**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)

            log(f"(FAIL) {interaction.user} failed to use the /modrinth command (Invalid project's slug or ID?)")

        title = res['title'] or None
        description = res['description'] or None
        project_type = res['project_type'].capitalize() or None
        project_id = res['id'] or None
        project_slug = res['slug'] or None
        license = res['license']['id'] or None
        client_compatibility = res['client_side'].capitalize() or None
        server_compatibility = res['server_side'].capitalize() or None
        downloads = "{:,.2f}".format(res['downloads']).split('.')[0] or None
        followers = "{:,.2f}".format(res['followers']).split('.')[0] or None

        if res["license"]["url"] != None:
            license = f"[{license}]({res['license']['url']})"

        view = View()

        button = Button(label='Webpage', style=ButtonStyle.url, url=f"https://modrinth.com/{res['project_type']}/{project_slug}")
        view.add_item(button)

        if "wiki_url" in res and res['wiki_url'] != None:
            button = Button(label='Wiki', style=ButtonStyle.url, url=f"{res['wiki_url']}")
            view.add_item(button)

        if "discord_url" in res and res['discord_url'] != None:
            button = Button(label='Discord', style=ButtonStyle.url, url=f"{res['discord_url']}")
            view.add_item(button)

        if "source_url" in res and res['source_url'] != None:
            button = Button(label='Source', style=ButtonStyle.url, url=f"{res['source_url']}")
            view.add_item(button)

        if "issues_url" in res and res['issues_url'] != None:
            button = Button(label='Issues', style=ButtonStyle.url, url=f"{res['issues_url']}")
            view.add_item(button)

        for donation_url in res['donation_urls']:

            if donation_url['id'] == "patreon":
                button = Button(label=donation_url['platform'], style=ButtonStyle.url, url=donation_url['url'])
                view.add_item(button)
            elif donation_url['id'] == "bmac":
                button = Button(label="Buy Me a Coffee", style=ButtonStyle.url, url=donation_url['url'])
                view.add_item(button)
            elif donation_url['id'] == "paypal":
                button = Button(label=donation_url['platform'], style=ButtonStyle.url, url=donation_url['url'])
                view.add_item(button)
            elif donation_url['id'] == "github":
                button = Button(label="GitHub Sponsors", style=ButtonStyle.url, url=donation_url['url'])
                view.add_item(button)
            elif donation_url['id'] == "ko-fi":
                button = Button(label=donation_url['platform'], style=ButtonStyle.url, url=donation_url['url'])
                view.add_item(button)
            elif donation_url['id'] == "other":
                button = Button(label="Donate", style=ButtonStyle.url, url=donation_url['url'])
                view.add_item(button)

        embed = Embed(title=f'{title}',description=f'> **{description}**\n\n**Project Type:** {project_type}\n**Project ID:** {project_id}\n**Project Slug:** {project_slug}\n**License:** {license}\n\n**Client compatibility:** {client_compatibility}\n**Server compatibility:** {server_compatibility}\n\n**Downloads:** {downloads}\n**Followers** {followers}\n\n',colour=res["color"])
        embed.set_thumbnail(url=res['icon_url'])
        embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}")
        embed.timestamp = datetime.now()
        await interaction.response.send_message(" ",embed=embed, view=view)

        log(f"(SUCCESS) {interaction.user} used /modrinth")