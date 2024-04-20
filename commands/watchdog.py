from discord import Interaction, Embed
from discord.app_commands import default_permissions, allowed_contexts, allowed_installs
from util.functions import log
from requests import get as requestGet
from util.resources import api_key
from datetime import datetime

def commandFunction(tree, client):
    @tree.command(name="watchdog",description="Show the Hypixel Watchdog Anticheat's stats")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def watchdogCommand(interaction: Interaction):
        res = requestGet(
            url="https://api.hypixel.net/punishmentstats",
            params= {
                "key":api_key
            }
        ).json()

        if res["success"] == True:
            embed = Embed(title=" ",description="**Getting data from the API, please wait...**",colour=9807270)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            embed = Embed(title=f"**Watchdog Stats**",description=f'> **Total players banned by Watchdog in the last minute:** ``{res["watchdog_lastMinute"]}``\n> **Total players banned by Watchdog today:** ``{res["watchdog_rollingDaily"]}``\n> **Total players banned by Watchdog:** ``{res["watchdog_total"]}``\n\n> **Total players banned by Hypixel Staff Members today:** ``{res["staff_rollingDaily"]}``\n> **Total players banned by Hypixel Staff Members:** ``{res["staff_total"]}``')
            embed.set_thumbnail(url=f"https://yt3.googleusercontent.com/ytc/AIf8zZSv_62EYjr0w3lqr0PydI8vBsdscbUlMCYyWghH6g=s176-c-k-c0x00ffffff-no-rj")
            embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}")
            embed.timestamp = datetime.now()
            await interaction.channel.send(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} used /watchdog")
                
        elif res["success"] == False:
            if res["cause"] == "Invalid API key":
                embed = Embed(title=" ",description=":x: **Couldn't connect to the Hypixel API. Please try again in a few moments.**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)

                log(f"(FAIL) {interaction.user} failed to use the /watchdog command (Invalid API Key)")

            elif res["cause"] == "Key throttle":
                embed = Embed(title=" ",description=":x: **Too much requests. Please try again in a few moments.**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)

                log(f"(FAIL) {interaction.user} failed to use the /watchdog command (Key throttle)")

            elif res["cause"] == "Leaderboard data has not yet been populated":
                embed = Embed(title=" ",description=":x: **Data has not been published yet. Please try again in a few moments.**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)

                log(f"(FAIL) {interaction.user} failed to use the /watchdog command (Leaderboard data has not yet been populated)")
        else:
            embed = Embed(title=" ",description=":x: **Something went wrong. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            
            log(f"(FAIL) {interaction.user} failed to use the /watchdog command")