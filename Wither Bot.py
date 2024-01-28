import datetime
import json
import random
import discord
import requests
from discord import Embed, app_commands, ui , Webhook
from discord_together import DiscordTogether
from discord import *
from discord.ext import tasks
from discord.ui import Button, Modal, View, Select
from discord.utils import get

class ban_form(discord.ui.Modal, title='Ban'):
    def __init__(self, member:discord.Member):
        self.member = member
        super().__init__()
    input_0 = ui.TextInput(label="Ban Reason",placeholder="'None' if no reasons are provided",style=TextStyle.long, required=False)
    async def on_submit(self, interaction: discord.Interaction):
        try:
            if self.input_0.value == "":
                try:
                    embed = discord.Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.ban(reason=self.input_0.value)
                embed = discord.Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{self.member}`` has been banned from the server!**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)

                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} BANNED {self.member} on {interaction.user.guild} ({interaction.user.guild.id})\n")
                f.close()
                
            else:
                try:
                    embed = discord.Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**\n``Reason: {self.input_0.value}``",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.ban(reason=self.input_0.value)
                embed = discord.Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{self.member}`` has been banned from the server!**\n**``Reason: {self.input_0.value}``**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} BANNED {self.member} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
                f.close()
        
        except:
            embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the ban application\n")
            f.close()

class kick_form(discord.ui.Modal, title='Kick'):
    def __init__(self, member:discord.Member):
        self.member = member
        super().__init__()
    input_0 = ui.TextInput(label="Kick Reason",placeholder="'None' if no reasons are provided",style=TextStyle.long, required=False)
    async def on_submit(self, interaction: discord.Interaction):
        try:
            if self.input_0.value == "":
                try:
                    embed = discord.Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.kick(reason=self.input_0.value)
                embed = discord.Embed(title=" ",description=f"**``{self.member}`` has been kicked from the server!**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} BANNED {self.member} on {interaction.user.guild} ({interaction.user.guild.id})\n")
                f.close()
                
            else:
                try:
                    embed = discord.Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**\n``Reason: {self.input_0.value}``",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.kick(reason=self.input_0.value)
                embed = discord.Embed(title=" ",description=f"**``{self.member}`` has been kicked from the server!**\n**``Reason: {self.input_0.value}``**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} KICKED {self.member} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
                f.close()
        
        except:
            embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the kick application\n")
            f.close()

class timeout_form(discord.ui.Modal, title='Timeout'):
    def __init__(self, member:discord.Member):
        self.member = member
        super().__init__()
    input_0 = ui.TextInput(label="Timeout Reason",placeholder="'None' if no reasons are provided",style=TextStyle.long, required=False)
    input_1 = ui.TextInput(label="Days",placeholder="How long will be the timeout (in days, maximum of 28 days)",style=TextStyle.short, required=False)
    input_2 = ui.TextInput(label="Hours",placeholder="How long will be the timeout (in hours)",style=TextStyle.short, required=False)
    input_3 = ui.TextInput(label="Minutes",placeholder="How long will be the timeout (in minutes)",style=TextStyle.short, required=False)
    input_4 = ui.TextInput(label="Seconds",placeholder="How long will be the timeout (in seconds)",style=TextStyle.short, required=False)
    async def on_submit(self, interaction: discord.Interaction):
        if self.input_1.value == "":
            days = 0
        else:
            days = int(self.input_1.value)
        
        if self.input_2.value == "":
            hours = 0
        else:
            hours = int(self.input_2.value)

        if self.input_3.value == "":
            minutes = 0
        else:
            minutes = int(self.input_3.value)

        if self.input_4.value== "":
            seconds = 0
        else:
            seconds = int(self.input_4.value)

        if days+hours+minutes+seconds == 0:
            days = 7

        timedelta = datetime.timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        try:
            if self.input_0.value == "":
                await self.member.timeout(timedelta,reason=self.input_0.value)
                await interaction.response.send_message(" ",embed=discord.Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{self.member.id}> **for {days}d {hours}h {minutes}m {seconds}s**", colour=5763719))
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} MUTED {self.member} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id})\n")
                f.close()
                try:
                    await self.member.send(" ",embed=discord.Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**",description="", colour=15548997))
                except:
                    await interaction.channel.send(" ",embed=discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997))
            else:
                await self.member.timeout(timedelta,reason=self.input_0.value)
                await interaction.response.send_message(" ",embed=discord.Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{user.id}> **for {days}d {hours}h {minutes}m {seconds}s**\n``Reason: {self.input_0.value}``", colour=5763719))
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} MUTED {self.member} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
                f.close()
                try:
                    await self.member.send(" ",embed=discord.Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**\n``Reason: {self.input_0.value}``",description="", colour=15548997))
                except:
                    await interaction.channel.send(" ",embed=discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997))
        except:
            await interaction.response.send_message(" ",embed=discord.Embed(title=" ",description=":x: **An error occurred**", colour=15548997))
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the timeout application\n")
            f.close()
        
with open ("config.json", "r") as config_file:
    config_data = json.load(config_file)
    TOKEN = config_data["token"]
    api_key = config_data["api_key"]

with open ("items.json", "r") as items_file:
    items_data = json.load(items_file)
    ITEMS = items_data["items"]

with open ("blocks.json", "r") as blocks_file:
    blocks_data = json.load(blocks_file)
    BLOCKS = blocks_data["blocks"]

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Logged in as {self.user}.")
        await client.change_presence(activity=discord.Game(name="with command blocks"))
        tree.togetherControl = await DiscordTogether(TOKEN)
        channel = client.get_channel(1040593202060730519)
        embed = discord.Embed(title=" ",description=f"**``{self.user}, has appeared.``\nPing: {round (client.latency * 1000)} ms**")
        f = open("logs.txt", "a")
        f.write(f"\n[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {self.user} has been STARTED. Ping: {round (client.latency * 1000)} ms\n")
        f.close()
        await channel.send(" ", embed=embed)

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name= "ping", description= "Show the latency between the host and Discord")
async def pingCommand(interaction: discord.Interaction):
    embed = discord.Embed(title=" ",description=f"<:ping_pong:1039884406552268882> **{round (client.latency * 1000)} ms**", colour=5763719)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} PINGED the bot: {round (client.latency * 1000)} ms\n")
    f.close()

@tree.command(name= "ban", description= "Ban someone on your Discord server")
@app_commands.default_permissions(ban_members = True)
async def banCommand(interaction: discord.Interaction, user: discord.Member, reason:str = None):
    if interaction.user.id == user.id:
        embed = discord.Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban yourself!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to BAN himself on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    elif 1039238934682665030 == user.id:
        embed = discord.Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban me!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to BAN the bot on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    else:
        try:
            if reason == None:
                try:
                    embed = discord.Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**",description="", colour=15548997)
                    await user.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await user.ban(reason=reason)
                embed = discord.Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                await interaction.channel.send(" ",embed=embed2)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} has BANNED {user} on {interaction.user.guild} ({interaction.user.guild.id})\n")
                f.close()
                
            else:
                try:
                    embed = discord.Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**\n``Reason: {reason}``",description="", colour=15548997)
                    await user.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await user.ban(reason=reason)
                embed = discord.Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**\n**``Reason: {reason}``**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                await interaction.channel.send(" ",embed=embed2)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} has BANNED {user} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
                f.close()
        except:
            embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} has failed using the /ban command\n")
            f.close()

@tree.command(name= "kick", description= "Kick someone from your Discord server")
@app_commands.default_permissions(kick_members = True)
async def kickCommand(interaction: discord.Interaction, user: discord.Member, reason:str = None):
    if interaction.user.id == user.id:
        embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick yourself!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to KICK himself on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    elif 1039238934682665030 == user.id:
        embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick me!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to KICK the bot on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    else:
        try:
            if reason == None:
                try:
                    embed = discord.Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**",description="", colour=15548997)
                    await user.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await interaction.channel.send(" ",embed=embed)
                await user.kick(reason=reason)
                embed = discord.Embed(title=" ",description=f"**``{user}`` has been kicked from the server!**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                await interaction.channel.send(" ",embed=embed2)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} has KICKED {user} on {interaction.user.guild} ({interaction.user.guild.id})\n")
                f.close()
            else:
                try:
                    embed = discord.Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**\n``Reason: {reason}``",description="", colour=15548997)
                    await user.send(" ",embed=embed)
                except:
                    embed2 = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await user.kick(reason=reason)
                embed = discord.Embed(title=" ",description=f"**``{user}`` has been kicked from the server!**\n**``Reason: {reason}``**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                await interaction.channel.send(" ",embed=embed2)
                f = open("logs.txt", "a")
                f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} has KICKED {user} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
                f.close()
        
        except:
            embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} has failed using the /kick command\n")
            f.close()

@tree.command(name= "fakeban", description= "Fakeban someone on your Discord server")
@app_commands.default_permissions(ban_members = True)
async def fakeBanCommand(interaction: discord.Interaction, user: discord.Member, reason:str = None):
    if reason == None:
        embed = discord.Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**", colour=5763719)
        await interaction.response.send_message(" ",embed=embed)
        embed = discord.Embed(title=" ",description=f"**You have been <:gregban:1039247298808520794> fakebanned from ``{interaction.guild.name}``.**")
        await user.send(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} has FAKEBANNED {user} on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    else:
        embed = discord.Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{user}`` has been banned from the server!**\n**``Reason: {reason}``**", colour=5763719)
        await interaction.response.send_message(" ",embed=embed)
        embed = discord.Embed(title=" ",description=f"**You have been <:gregban:1039247298808520794> fakebanned from ``{interaction.guild.name}``\n**``Reason: {reason}``**.**")
        await user.send(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} has FAKEBANNED {user} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
        f.close()

@tree.command(name= "skyblock_ehp", description= "Calculate your EHP in SkyBlock")
async def skyblockEhpCommand(interaction: discord.Interaction, health: int, defense: int):
    ehp = health*(1+defense/100)
    embed = discord.Embed(title=" ",description=f"**Your EHP is {ehp}** ({health} ❤ Health and {defense} ❈ Defense)", colour=2067276)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_ehp\n")
    f.close()

@tree.command(name= "skyblock_damage_reduction", description= "Calculate your Damage Reduction percentage in SkyBlock")
async def skyblockDamageReductionCommand(interaction: discord.Interaction, defense: int):
    damage_reduction = round(defense/(defense+100)*100,2)
    embed = discord.Embed(title=" ",description=f"**Your Damage Reduction percentage is {damage_reduction}%** ({defense} ❈ Defense)", colour=2067276)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_damage_reduction\n")
    f.close()

@tree.command(name= "skyblock_true_damage_reduction", description= "Calculate your True Damage Reduction percentage in SkyBlock")
async def skyblockTrueDamageReductionCommand(interaction: discord.Interaction, true_defense: int):
    true_damage_reduction = round(true_defense/(true_defense+100)*100,2)
    embed = discord.Embed(title=" ",description=f"**Your True Damage Reduction percentage is {true_damage_reduction}%** ({true_defense} ❂ True Defense)", colour=16777215)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_true_damage_reduction\n")
    f.close()

@tree.command(name= "skyblock_base_mana_regeneration", description= "Calculate your Base Mana Regeneration in SkyBlock")
async def skyblockBaseManaRegenerationCommand(interaction: discord.Interaction, mana: int):
    base_mana_regeneration = mana * 0.02
    embed = discord.Embed(title=" ",description=f"**Your Mana Regeneration rate is {base_mana_regeneration} ✎ Mana/s** ({mana} ✎ Mana)", colour=3447003)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_base_mana_regeneration\n")
    f.close()

@tree.command(name= "skyblock_base_hp_regeneration", description= "Calculate your Base Health Regeneration in SkyBlock")
async def skyblockBaseHpRegenerationCommand(interaction: discord.Interaction, health: int):
    base_health_regeneration = ((health*0.01)+1.5)
    embed = discord.Embed(title=" ",description=f"**Your Health Regeneration rate is {base_health_regeneration} ❤ Health/s** ({health} ❤ Health)", colour=15548997)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_base_hp_regeneration\n")
    f.close()

@tree.command(name= "skyblock_dungeons_requirement", description= "Show the Catacombs Level Requirements in SkyBlock")
async def skyblockDungeonsRequirementsCommand(interaction: discord.Interaction):
    embed = discord.Embed(title="Dungeon Levels Requirement",description="")
    embed.add_field(name="\n<:f0:1040298722103398440> Entrance", value="\nCombat Level 15", inline=False)
    embed.add_field(name="\n<:f1:1040298723667890277> Floor 1", value="\nCatacombs Level 1", inline=False)
    embed.add_field(name="\n<:f2:1040298724968120390> Floor 2", value="\nCatacombs Level 3", inline=False)
    embed.add_field(name="\n<:f3:1040298726209638500> Floor 3", value="\nCatacombs Level 5", inline=False)
    embed.add_field(name="\n<:f4:1040298727551803433> Floor 4", value="\nCatacombs Level 9", inline=False)
    embed.add_field(name="\n<:f5:1040298729309229136> Floor 5", value="\nCatacombs Level 14", inline=False)
    embed.add_field(name="\n<:f6:1040298730080968765> Floor 6", value="\nCatacombs Level 19", inline=False)
    embed.add_field(name="\n<:f7:1040298731867734079> Floor 7", value="\nCatacombs Level 24", inline=False)
    embed.add_field(name="\n<:low_master_floor:1040298735047016559> Master Mode Floor 1", value="\nCatacombs Level 24", inline=False)
    embed.add_field(name="\n<:low_master_floor:1040298735047016559> Master Mode Floor 2", value="\nCatacombs Level 26", inline=False)
    embed.add_field(name="\n<:low_master_floor:1040298735047016559> Master Mode Floor 3", value="\nCatacombs Level 28", inline=False)
    embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 4", value="\nCatacombs Level 30", inline=False)
    embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 5", value="\nCatacombs Level 32", inline=False)
    embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 6", value="\nCatacombs Level 34", inline=False)
    embed.add_field(name="\n<:high_master_floor:1040298733302194196> Master Mode Floor 7", value="\nCatacombs Level 36", inline=False)
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_dungeons_requirement\n")
    f.close()

@tree.command(name= "say", description= "Say something")
@app_commands.default_permissions(manage_messages = True)
async def sayCommand(interaction: discord.Interaction, message: str):
    embed = discord.Embed(title=" ",description=f"**Message sent in <#{interaction.channel.id}>**", colour=5763719)
    await interaction.response.send_message(" ",embed=embed, ephemeral=True)
    await interaction.channel.send(message)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /say on {interaction.user.guild} ({interaction.user.guild.id})\n")
    f.close()

@tree.command(name= "addrole", description= "Add a role to someone on your Discord server")
@app_commands.default_permissions(manage_roles = True)
async def addRoleCommand(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    try:
        await member.add_roles(role)
        embed = discord.Embed(title=" ",description=f":white_check_mark: **Successfully added** ``{role}`` **to** ``{member}``**.**",colour=5763719)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} ADDED a role to {member} on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    except:
        embed = discord.Embed(title=" ",description=f":x: **An error occured**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use /addrole\n")
        f.close()


@tree.command(name= "removerole", description= "Remove a role from someone on your Discord server")
@app_commands.default_permissions(manage_roles = True)
async def removeRoleCommand(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    try:
        await member.remove_roles(role)
        embed = discord.Embed(title=" ",description=f":white_check_mark: **Successfully removed** ``{role}`` **from** ``{member}``**.**",colour=5763719)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} REMOVED a role from {member} on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    except:
        embed = discord.Embed(title=" ",description=f":x: **An error occured**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use /removerole\n")
        f.close()

@tree.command(name= "hello", description= "Hello!")
async def helloCommand(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello <@{interaction.user.id}>!")
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /hello\n")
    f.close()

@tree.command(name="skyblock_random_item",description="Choose a random SkyBlock item")
async def skyblockRandomItemCommand(interaction:discord.Interaction):
    items = requests.get(
        url="https://api.hypixel.net/resources/skyblock/items"
    ).json()
    ind = random.randint(1,4103)
    item = str(items["items"][ind]["name"])
    try:
        lore = str(items["items"][ind]["description"])+"\n"
    except:
        lore = ""
    try:
        rarity = str(items["items"][ind]["tier"])
    except:
        rarity = "None"
    embed = discord.Embed(title=" ",description=f"``{item}``\n{lore}**{rarity}**")
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /skyblock_random_item\n")
    f.close()
    #for i in range(len(items["items"])):
    #    if(items["items"][i]["name"] == "Very Scientific Paper"):
    #        print(i)
    #        print(items["items"][i])

@tree.command(name= "minecraft_random_item", description= "Choose a random item in Minecraft (1.17.1)")
async def minecraftRandomItemCommand(interaction: discord.Interaction):
    random_item = ITEMS[random.randint(0,len(ITEMS) - 1)]
    i = 0
    item_list = random_item.split("_")
    random_item = ""
    while(i < len(item_list)):
        item_item = item_list[i]
        item_item = item_item.replace(item_item[0], item_item[0].upper(), 1)
        random_item = f'{random_item} {item_item}'
        i = i + 1
    random_item = random_item.replace(" ", "", 1)
    embed = discord.Embed(title=" ",description=f"**{random_item}**")
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /minecraft_random_item\n")
    f.close()

@tree.command(name= "minecraft_random_block", description= "Choose a random block in Minecraft (1.17.1)")
async def minecraftRandomBlockCommand(interaction: discord.Interaction):
    random_block = BLOCKS[random.randint(0,len(BLOCKS) - 1)]
    i = 0
    block_list = random_block.split("_")
    random_block = ""
    while(i < len(block_list)):
        block_item = block_list[i]
        block_item = block_item.replace(block_item[0], block_item[0].upper(), 1)
        random_block = f'{random_block} {block_item}'
        i = i + 1
    random_block = random_block.replace(" ", "", 1)
    embed = discord.Embed(title=" ",description=f"**{random_block}**")
    await interaction.response.send_message(" ",embed=embed)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /minecraft_random_block\n")
    f.close()

@tree.command(name= "timeout", description= "Mute someone on your Discord server")
@app_commands.default_permissions(moderate_members = True)
async def timeoutCommand(interaction: discord.Interaction, user:discord.Member, reason: str = None, days:int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
    time = days + hours + minutes + seconds
    if time == 0:
        days = 7
    timedelta = datetime.timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
    if interaction.user.id == user.id:
        embed = discord.Embed(title=" ",description=f":x: **You cannot mute yourself!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to MUTE himself on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    elif 1039238934682665030 == user.id:
        embed = discord.Embed(title=" ",description=f":x: **You cannot mute me!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to MUTE the bot on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    try:
        if reason == None:
            await user.timeout(timedelta,reason=reason)
            embed = discord.Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{user.id}> **for {days}d {hours}h {minutes}m {seconds}s**", colour=5763719)
            await interaction.response.send_message(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} MUTED {user} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id})\n")
            f.close()
            try:
                embed = discord.Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**",description="", colour=15548997)
                await user.send(" ",embed=embed)
            except:
                embed = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await interaction.channel.send(" ",embed=embed)
        else:
            await user.timeout(timedelta,reason=reason)
            embed = discord.Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{user.id}> **for {days}d {hours}h {minutes}m {seconds}s**\n``Reason: {reason}``", colour=5763719)
            await interaction.response.send_message(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} MUTED {user} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason\n")
            f.close()
            try:
                embed = discord.Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**\n``Reason: {reason}``",description="", colour=15548997)
                await user.send(" ",embed=embed)
            except:
                embed = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await interaction.channel.send(" ",embed=embed)
    except:
        embed = discord.Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /timeout command\n")
        f.close()

@tree.command(name="unmute",description="Unmute someone on your Discord server")
@app_commands.default_permissions(moderate_members = True)
async def unmuteCommand(interaction:discord.Interaction, user:discord.Member):
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    timedelta = datetime.timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
    try:
        await user.timeout(timedelta, reason="Unmute")
        embed = discord.Embed(title=" ",description=f":white_check_mark: **Successfully unmuted** <@{user.id}>", colour=5763719)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} UNMUTED {user} on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
        try:
            embed = discord.Embed(title=f"**You have been unmuted on ``{interaction.guild.name}``**",description="", colour=5763719)
            await user.send(" ",embed=embed)
        except:
            embed = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
            await interaction.channel.send(" ",embed=embed)
    except:
        embed = discord.Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /unmute command\n")
        f.close()

@tree.command(name= "youtube", description= "Watch YouTube Together")
async def youtubeCommand(interaction: discord.Interaction):
    try:
        link = await tree.togetherControl.create_link(interaction.user.voice.channel.id, 'youtube')
        embed = discord.Embed(title="Watch Together: YouTube",description=f"Click the link below to start the activity\n{link}", colour=2067276)
        await interaction.response.send_message(" ", embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} started an activity (YouTube Together) on {interaction.user.guild} ({interaction.user.guild.id})\n")
        f.close()
    except:
        embed = discord.Embed(title=" ",description=":x: **An error occurred. Are you in a voice channel?**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /youtube command\n")
        f.close()

@tree.command(name="player",description="Show the stats of a Hypixel player.")
async def playerCommand(interaction: discord.Interaction, minecraft_username: str):
    try:
        uuid = requests.get(
        url="https://api.mojang.com/users/profiles/minecraft/"+minecraft_username
        ).json()["id"]
    except:
        embed = discord.Embed(title=" ",description=":x: **Something went wrong. Did you write the correct username?**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /player command (Invalid username)\n")
        f.close()

    res = requests.get(
        url="https://api.hypixel.net/player",
        params= {
            "key":api_key,
            "uuid": uuid
        }
        ).json()
    res2 = requests.get(
        url="https://api.hypixel.net/status",
        params= {
            "key":api_key,
            "uuid": uuid
        }
        ).json()
    
    res3 = requests.get(
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
            embed = discord.Embed(title=" ",description="**Getting player's data from the API, please wait...**",colour=9807270)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            embed = discord.Embed(title=f"**Online and playing**",description=f'**Game**: ``{game}\n``**Guild:** ``{guild}``\n**Rank:** ``{rank}``\n**Language:** ``{language}``\n**First Login:** {first_login}\n**Last Login:** {last_login}',colour=2067276)
            embed.set_author(name=f"{minecraft_username}'s Stats", icon_url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
            embed.set_thumbnail(url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
            embed.set_footer(text=f"Wither Bot", icon_url="https://static.wikia.nocookie.net/minecraft_fr_gamepedia/images/a/aa/Wither.png")
            embed.timestamp = datetime.datetime.now()
            await interaction.channel.send(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /player\n")
            f.close()

        else:
            embed = discord.Embed(title=" ",description="**Getting player's data from the API, please wait...**",colour=9807270)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            embed = discord.Embed(title="Offline or Invisible",description=f'**Guild:** ``{guild}``\n**Rank:** ``{rank}``\n**Language:** ``{language}``\n**First Login:** {first_login}\n**Last Login:** {last_login}',colour=9807270)
            embed.set_author(name=f"{minecraft_username}'s Stats", icon_url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
            embed.set_thumbnail(url=f"https://starlightskins.lunareclipse.studio/skin-render/pixel/{uuid}/face")
            embed.set_footer(text=f"Wither Bot", icon_url="https://static.wikia.nocookie.net/minecraft_fr_gamepedia/images/a/aa/Wither.png")
            embed.timestamp = datetime.datetime.now()
            await interaction.channel.send(" ",embed=embed)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /player\n")
            f.close()
            embed1 = discord.Embed(title=f" ",description=f'',colour=9807270)    
    elif res["success"] == False or res2["success"] == False or res3["success"] == False:
        if res["cause"] == "Invalid API key" or res2["cause"] == "Invalid API key" or res3["cause"] == "Invalid API key":
            embed = discord.Embed(title=" ",description=":x: **Couldn't connect to the Hypixel API. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /player command (Invalid API key)\n")
            f.close()

        elif res["cause"] == "Key throttle" or res2["cause"] == "Key throttle" or res3["cause"] == "Key throttle":
            embed = discord.Embed(title=" ",description=":x: **Too much requests. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /player command (Key throttle)\n")
            f.close()

    else:
        embed = discord.Embed(title=" ",description=":x: **Something went wrong. Please try again in a few moments.**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /player command\n")
        f.close()


@tree.command(name="credits",description="Show the credits of the bot")
async def creditsCommand(interaction: discord.Interaction):
    embed = discord.Embed(title=" ",description=f"**<@1039238934682665030> has been created by <@629711559899217950>**",colour=8359053)

    button = discord.ui.Button(label='Vote for the bot on top.gg', style=discord.ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
    button2 = discord.ui.Button(label='Invite the bot on your server', style=discord.ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
    view = View()
    view.add_item(button)
    view.add_item(button2)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /credits\n")
    f.close()

    await interaction.response.send_message(" ",embed=embed, view=view, ephemeral=True)

@tree.context_menu(name="Ban")
@app_commands.default_permissions(ban_members=True)
async def show_stats(interaction:discord.Interaction, user:discord.Member):
    if interaction.user.id == user.id:
        embed = discord.Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban yourself!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to BAN himself\n")
        f.close()
    elif 1039238934682665030 == user.id:
        embed = discord.Embed(title=" ",description=f"**You cannot <:gregban:1039247298808520794> ban me!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to BAN the bot\n")
        f.close()
    else:
        await interaction.response.send_modal(ban_form(user))

@tree.context_menu(name="Kick")
@app_commands.default_permissions(kick_members=True)
async def show_stats(interaction:discord.Interaction, user:discord.Member):
    if interaction.user.id == user.id:
        embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick yourself!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to KICK himself\n")
        f.close()
    elif 1039238934682665030 == user.id:
        embed = discord.Embed(title=" ",description="<:x:1039888272761049179> **You cannot kick me!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to KICK the bot\n")
        f.close()
    else:
        await interaction.response.send_modal(kick_form(user))

@tree.context_menu(name="Timeout")
@app_commands.default_permissions(moderate_members=True)
async def show_stats(interaction:discord.Interaction, user:discord.Member):
    if interaction.user.id == user.id:
        embed = discord.Embed(title=" ",description=f":x: **You cannot mute yourself!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to MUTE himself\n")
        f.close()
    elif 1039238934682665030 == user.id:
        embed = discord.Embed(title=" ",description=f":x: **You cannot mute me!**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} tried to MUTE the bot\n")
        f.close()
    else:
        await interaction.response.send_modal(timeout_form(user))

@tree.context_menu(name="Unmute")
@app_commands.default_permissions(moderate_members=True)
async def show_stats(interaction:discord.Interaction, user:discord.Member):
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    timedelta = datetime.timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
    try:
        await user.timeout(timedelta, reason="Unmuted")
        embed = discord.Embed(title=" ",description=f":white_check_mark: **Successfully unmuted** <@{user.id}>", colour=5763719)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} UNMUTED {user} on {interaction.user.guild.name} ({interaction.user.guild.id})\n")
        f.close()
        try:
            embed = discord.Embed(title=f"**You have been unmuted on ``{interaction.guild.name}``**",description="", colour=5763719)
            await user.send(" ",embed=embed)
        except:
            embed = discord.Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
            await interaction.channel.send(" ",embed=embed)
    except:
        embed = discord.Embed(title=" ",description=":x: **An error occurred**", colour=15548997)
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the mute application\n")
        f.close()

@tree.command(name="help",description="Show all the commands")
async def helpCommand(interaction: discord.Interaction):
    embed = discord.Embed(title="Bot commands",description="")
    embed.add_field(name="\n__General__", value="", inline=False)
    embed.add_field(name="\n/hello", value=f"\n{helloCommand.description}", inline=False)
    embed.add_field(name="\n/ping", value=f"\n{pingCommand.description}", inline=False)
    embed.add_field(name="\n/credits", value=f"\n{creditsCommand.description}", inline=False)
    embed.add_field(name="\n/youtube", value=f"\n{youtubeCommand.description}", inline=False)
    embed.add_field(name="\n/invite", value=f"\n{inviteCommand.description}", inline=False)
    embed.add_field(name="\n/vote", value=f"\n{voteCommand.description}\n", inline=False)

    embed.add_field(name="\n__Moderation__", value="", inline=False)
    embed.add_field(name="\n/ban", value=f"\n{banCommand.description}", inline=False)
    embed.add_field(name="\n/kick", value=f"\n{kickCommand.description}", inline=False)
    embed.add_field(name="\n/say", value=f"\n{sayCommand.description}", inline=False)
    embed.add_field(name="\n/addrole", value=f"\n{addRoleCommand.description}", inline=False)
    embed.add_field(name="\n/removerole", value=f"\n{removeRoleCommand.description}", inline=False)
    embed.add_field(name="\n/timeout", value=f"\n{timeoutCommand.description}", inline=False)
    embed.add_field(name="\n/unmute", value=f"\n{unmuteCommand.description}\n", inline=False)

    embed.add_field(name="\n__Hypixel / Skyblock__", value="", inline=False)
    embed.add_field(name="\n/skyblock_ehp", value=f"\n{skyblockEhpCommand.description}", inline=False)
    embed.add_field(name="\n/skyblock_damage_reduction", value=f"\n{skyblockDamageReductionCommand.description}", inline=False)
    embed.add_field(name="\n/skyblock_true_damage_reduction", value=f"\n{skyblockTrueDamageReductionCommand.description}", inline=False)
    embed.add_field(name="\n/skyblock_base_mana_regeneration", value=f"\n{skyblockBaseManaRegenerationCommand.description}", inline=False)
    embed.add_field(name="\n/skyblock_base_hp_regeneration", value=f"\n{skyblockBaseHpRegenerationCommand.description}", inline=False)
    embed.add_field(name="\n/skyblock_dungeons_requirement", value=f"\n{skyblockDungeonsRequirementsCommand.description}", inline=False)
    embed.add_field(name="\n/skyblock_random_item", value=f"\n{skyblockRandomItemCommand.description}", inline=False)

    embed2 = discord.Embed(title=" ",description="")
    embed2.add_field(name="\n/player", value=f"\n{playerCommand.description}", inline=False)
    embed2.add_field(name="\n/watchdog", value=f"\n{watchdogCommand.description}\n", inline=False)
    embed2.add_field(name="\n__Minecraft__", value="", inline=False)
    embed2.add_field(name="\n/modrinth", value=f"\n{modrinthCommand.description}", inline=False)
    embed2.add_field(name="\n/minecraft_random_item", value=f"\n{minecraftRandomItemCommand.description}", inline=False)
    embed2.add_field(name="\n/minecraft_random_block", value=f"\n{minecraftRandomBlockCommand.description}", inline=False)

    button = discord.ui.Button(label='Vote for the bot on top.gg', style=discord.ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
    button2 = discord.ui.Button(label='Invite the bot on your server', style=discord.ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
    view = View()
    view.add_item(button)
    view.add_item(button2)
    await interaction.response.send_message(" ",embed=embed)
    await interaction.channel.send(" ",embed=embed2, view=view)
    f = open("logs.txt", "a")
    f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /help\n")
    f.close()

@tree.command(name="watchdog",description="Show the Hypixel Watchdog Anticheat's stats")
async def watchdogCommand(interaction: discord.Interaction):
    res = requests.get(
        url="https://api.hypixel.net/punishmentstats",
        params= {
            "key":api_key
        }
    ).json()

    if res["success"] == True:
        embed = discord.Embed(title=" ",description="**Getting data from the API, please wait...**",colour=9807270)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        embed = discord.Embed(title=f"**Watchdog Stats**",description=f'> **Total players banned by Watchdog in the last minute:** ``{res["watchdog_lastMinute"]}``\n> **Total players banned by Watchdog today:** ``{res["watchdog_rollingDaily"]}``\n> **Total players banned by Watchdog:** ``{res["watchdog_total"]}``\n\n> **Total players banned by Hypixel Staff Members today:** ``{res["staff_rollingDaily"]}``\n> **Total players banned by Hypixel Staff Members:** ``{res["staff_total"]}``')
        embed.set_thumbnail(url=f"https://yt3.googleusercontent.com/ytc/AIf8zZSv_62EYjr0w3lqr0PydI8vBsdscbUlMCYyWghH6g=s176-c-k-c0x00ffffff-no-rj")
        embed.set_footer(text=f"Wither Bot", icon_url="https://static.wikia.nocookie.net/minecraft_fr_gamepedia/images/a/aa/Wither.png")
        embed.timestamp = datetime.datetime.now()
        await interaction.channel.send(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /watchdog\n")
        f.close()
            
    elif res["success"] == False:
        if res["cause"] == "Invalid API key":
            embed = discord.Embed(title=" ",description=":x: **Couldn't connect to the Hypixel API. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /watchdog command (Invalid API Key)\n")
            f.close()

        elif res["cause"] == "Key throttle":
            embed = discord.Embed(title=" ",description=":x: **Too much requests. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /watchdog command (Key throttle)\n")
            f.close()

        elif res["cause"] == "Leaderboard data has not yet been populated":
            embed = discord.Embed(title=" ",description=":x: **Data has not been published yet. Please try again in a few moments.**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
            f = open("logs.txt", "a")
            f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /watchdog command (Leaderboard data has not yet been populated)\n")
            f.close()

    else:
        embed = discord.Embed(title=" ",description=":x: **Something went wrong. Please try again in a few moments.**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /watchdog command\n")
        f.close()

@tree.command(name="modrinth",description="Search a project on Modrinth with its ID or its slug")
async def modrinthCommand(interaction: discord.Interaction, query: str):
    try:
        res = requests.get(
            url="https://api.modrinth.com/v2/project/"+query
        ).json()

        embed = discord.Embed(title=f'{res["title"]}',description=f'> **{res["description"]}**\n\n**Type:** ``{res["project_type"]}``\n**Project ID:** ``{res["id"]}``\n**Project Slug:** ``{res["slug"]}``\n**License:** ``{res["license"]["id"]}``\n\n**Client compatibility:** ``{res["client_side"]}``\n**Server compatibility:** ``{res["server_side"]}``\n\n**Downloads:** ``{res["downloads"]}``\n**Followers** ``{res["followers"]}``\n\n',colour=2067276)
        embed.set_thumbnail(url=res["icon_url"])
        embed.set_footer(text=f"Wither Bot", icon_url="https://static.wikia.nocookie.net/minecraft_fr_gamepedia/images/a/aa/Wither.png")
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(" ",embed=embed)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (SUCCESS) {interaction.user} used /modrinth\n")
        f.close()

    except:
        embed = discord.Embed(title=" ",description=":x: **Couldn't find the project. Have you entered the project's slug or ID correctly?**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        f = open("logs.txt", "a")
        f.write(f"[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (FAIL) {interaction.user} failed to use the /modrinth command (Invalid project's slug or ID?)\n")
        f.close()

@tree.command(name="invite",description="Invite the bot on your server!")
async def inviteCommand(interaction: discord.Interaction):
    embed = discord.Embed(title=" ",description="**Click the button below to add the bot to your server!**")
    button = discord.ui.Button(label='Invite the bot on your server!', style=discord.ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
    view = View()
    view.add_item(button)
    await interaction.response.send_message(" ",embed=embed, view=view)

@tree.command(name="vote",description="Vote for the bot on top.gg!")
async def voteCommand(interaction: discord.Interaction):
    embed = discord.Embed(title=" ",description="**Click the button below to vote for the bot on top.gg!**")
    button = discord.ui.Button(label='Vote for the bot on top.gg!', style=discord.ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
    view = View()
    view.add_item(button)
    await interaction.response.send_message(" ",embed=embed, view=view)

@tree.command(name="delete_logs",description="A command used by M336 to clear the logs")
@app_commands.default_permissions(administrator=True)
async def deleteLogsCommand(interaction: discord.Interaction):
    if interaction.user.id != 629711559899217950:
        embed = discord.Embed(title=" ",description="**:x: You cannot use this command!**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
    elif interaction.guild.id != 1191505948959842344:
        embed = discord.Embed(title=" ",description="**:x: You cannot use this command here!**",colour=15548997)
        await interaction.response.send_message(" ",embed=embed, ephemeral=True)
    else:
        try:
            f = open("logs.txt", "w")
            f.write(f"\n[{datetime.date.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}] (RESET) Logs have been RESET\n")
            f.close()
            embed = discord.Embed(title=" ",description="**Logs have been reset!**",colour=2067276)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
        except:
            embed = discord.Embed(title=" ",description="**:x: An error has occured while trying to reset the logs**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed, ephemeral=True)
client.run(TOKEN)