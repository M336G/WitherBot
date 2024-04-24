from discord import Interaction, Embed, File
from discord.app_commands import allowed_contexts, allowed_installs
from util.resources import users
from util.functions import log, logUser
from datetime import date, datetime
from subprocess import Popen, PIPE, run

def commandFunction(tree, client):
    @tree.command(name= "status", description="Display the bot's status")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ping(interaction: Interaction, options: str = ""):
        logUser(interaction.user.id)
        if "cmd:" in options:
            if interaction.user.id != 629711559899217950:
                embed = Embed(title=" ",description="**:x: You cannot use this command!**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(FAIL) {interaction.user} FAILED to use /status (not allowed (cmd))")
                return
            try:
                await interaction.response.send_message(Popen(options.split(":")[1], shell=True, stdout=PIPE).stdout.read().decode("utf-8").strip(), ephemeral=True)
                log(f"(SUCCESS) {interaction.user} used /status (successfully execute a command)")
                return
            except:
                embed = Embed(title=" ",description="**:x: An error has occured while trying to execute the command**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(FAIL) {interaction.user} FAILED to use /status (could not execute a command)")
                return
            
        elif options == "logs:delete":
            if interaction.user.id != 629711559899217950:
                embed = Embed(title=" ",description="**:x: You cannot use this command!**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(FAIL) {interaction.user} FAILED to use /status (not allowed (logs:delete))")
                return
            try:
                f = open("logs.txt", "w")
                f.write(f"[{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M:%S')}] (RESET) Logs have been RESET\n")
                f.close()
                embed = Embed(title=" ",description="**Logs have been deleted!**",colour=2067276)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(SUCCESS) {interaction.user} used /status (successfully deleted logs)")
                return
            except:
                embed = Embed(title=" ",description="**:x: An error has occured while trying to reset the logs**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(FAIL) {interaction.user} FAILED to use /status (could not delete logs)")
                return
            
        elif options == "logs":
            if interaction.user.id != 629711559899217950:
                embed = Embed(title=" ",description="**:x: You cannot use this command!**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(FAIL) {interaction.user} FAILED to use /status (not allowed (logs))")
                return
            try:
                logs = open(f"logs.txt", "rb")
            except:
                embed = Embed(title=" ",description="**:x: An error has occured while trying to reset the logs**",colour=15548997)
                await interaction.response.send_message(" ",embed=embed, ephemeral=True)
                log(f"(FAIL) {interaction.user} FAILED to use /status (could not retrieve logs)")
                return
            
            await interaction.response.send_message(file=File(logs), ephemeral=True)
            logs.close()
            log(f"(SUCCESS) {interaction.user} used /status (successfully sent logs)")
            return
        else:
            embed = Embed(title=f"",description=f"", colour=2067276)
            embed.set_author(name=f"{client.user.name}'s Status", icon_url=f"{client.user.avatar}")
            embed.add_field(name="> Response time", value=f"``{round (client.latency * 1000)} ms``", inline=True)
            embed.add_field(name="> Server Count", value=f"``{str(len(client.guilds))}``", inline=True)
            embed.add_field(name="> Unique users", value=f"``{str(len(users))}``", inline=True)
            embed.set_footer(text=f"{client.user.name}", icon_url=f"{client.user.avatar}")
            embed.timestamp = datetime.now()
            await interaction.response.send_message(" ",embed=embed)
            log(f"(SUCCESS) {interaction.user} used /status")
            return
