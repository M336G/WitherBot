from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from requests import get
from util.functions import log, logUser
from datetime import datetime

def commandFunction(tree, client):
    @tree.command(name= "httpcat", description= "Cool cat images inspired by HTTP Error codes!")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def httpCatCommand(interaction:Interaction, code:int):
        logUser(interaction.user.id)

        req = get(url=f"https://http.cat/{code}.jpg")

        if req.status_code != 200:
            embed = Embed(title=" ", description=":x: **Could not find any cat images with this HTTP error code!**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)

            log(f"(FAIL) {interaction.user} failed to use the /httpcat command (Invalid error code)")
            return

        embed = Embed(title=f"Error: {code}", description=" ", url=req.url)
        embed.set_image(url=f"{req.url}")
        embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}") 
        embed.timestamp = datetime.now()
        await interaction.response.send_message(" ",embed=embed)
            
        log(f"(SUCCESS) {interaction.user} used the /httpcat command")
