from discord import Interaction, Embed
from requests import get as requestGet
from util.functions import log
from util.resources import api_key
from datetime import datetime

def commandFunction(tree, client):
    @tree.command(name="player",description="Show the stats of a Hypixel player.")
    async def playerCommand(interaction: Interaction, minecraft_username: str):
        try:
            uuid = requestGet(
            url="https://api.mojang.com/users/profiles/minecraft/"+minecraft_username
            ).json()["id"]
        except:
            embed = Embed(title=" ",description=":x: **Something went wrong. Did you write the correct username?**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)

            log(f"(FAIL) {interaction.user} failed to use the /player command (Invalid username)")

        res = requestGet(
            url="https://api.hypixel.net/player",
            params= {
                "key":api_key,
                "uuid": uuid
            }
            ).json()
        res2 = requestGet(
            url="https://api.hypixel.net/status",
            params= {
                "key":api_key,
                "uuid": uuid
            }
            ).json()
        
        res3 = requestGet(
            url="https://api.hypixel.net/guild",
            params= {
                "key":api_key,
                "player": uuid
            }
            ).json()

        if res["success"] == True and res2["success"] == True and res3["success"] == True:
            if "rank" in res["player"]:
                rank = res["player"]["rank"]

            elif "newPackageRank" in res["player"]:
                if res["player"]["newPackageRank"] == "MVP_PLUS":
                    rank = "MVP_PLUS"
                    if "monthlyPackageRank" in res["player"]:
                        if res["player"]["monthlyPackageRank"] == "SUPERSTAR":
                            rank = "MVP_PLUS_PLUS"
                else:
                    rank = res["player"]["newPackageRank"]

            else:
                rank = "NONE"

            first_login = "``NONE``"
            last_login = "``NONE``"
            language = "NONE"
            game = "NONE"

            if "firstLogin" in res["player"]:
                first_login = int(int(res["player"]["firstLogin"])/1000)
                first_login = f"<t:{first_login}:R>"
            if "lastLogin" in res["player"]:
                last_login = int(int(res["player"]["lastLogin"])/1000)
                last_login = f"<t:{last_login}:R>"
            if "userLanguage" in res["player"]:
                language = res["player"]["userLanguage"]
            if "gameType" in res2["session"]:
                game = res2["session"]["gameType"]
                if game == "SKYBLOCK":
                    game = f"SKYBLOCK - " + res2["session"]["mode"]

            if res3["guild"] != None:
                guild = res3["guild"]["name"]
            else:
                guild = "NONE"

            if res2["session"]["online"] == True:
                embed = Embed(title=" ",description="**Getting player's data from the API, please wait...**",colour=9807270)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                embed = Embed(title=f"**Online and playing**",description=f'**Game**: ``{game}\n``**Guild:** ``{guild}``\n**Rank:** ``{rank}``\n**Language:** ``{language}``\n**First Login:** {first_login}\n**Last Login:** {last_login}',colour=2067276)
                embed.set_author(name=f"{minecraft_username}'s Stats", icon_url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
                embed.set_thumbnail(url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
                embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}")
                embed.timestamp = datetime.now()
                await interaction.channel.send(" ",embed=embed)

                log(f"(SUCCESS) {interaction.user} used /player")

            else:
                embed = Embed(title=" ",description="**Getting player's data from the API, please wait...**",colour=9807270)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                embed = Embed(title="Offline or Invisible",description=f'**Guild:** ``{guild}``\n**Rank:** ``{rank}``\n**Language:** ``{language}``\n**First Login:** {first_login}\n**Last Login:** {last_login}',colour=9807270)
                embed.set_author(name=f"{minecraft_username}'s Stats", icon_url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
                embed.set_thumbnail(url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
                embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}")
                embed.timestamp = datetime.now()
                await interaction.channel.send(" ",embed=embed)

                log(f"(SUCCESS) {interaction.user} used /player")
                embed1 = Embed(title=f" ",description=f'',colour=9807270)    
        elif res["success"] == False or res2["success"] == False or res3["success"] == False:
            if res["cause"] == "Invalid API key" or res2["cause"] == "Invalid API key" or res3["cause"] == "Invalid API key":
                embed = Embed(title=" ",description=":x: **Couldn't connect to the Hypixel API. Please try again in a few moments.**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)

                log(f"(FAIL) {interaction.user} failed to use the /player command (Invalid API key)")

            elif res["cause"] == "Key throttle" or res2["cause"] == "Key throttle" or res3["cause"] == "Key throttle":
                embed = Embed(title=" ",description=":x: **Too much requests. Please try again in a few moments.**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)

                log(f"(FAIL) {interaction.user} failed to use the /player command (Key throttle)")


        else:
            embed = Embed(title=" ",description=":x: **Something went wrong. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            
            log(f"(FAIL) {interaction.user} failed to use the /player command")
        