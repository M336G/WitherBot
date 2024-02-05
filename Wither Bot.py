from discord_together import DiscordTogether
from discord import Client, Intents, Game, Embed 
from discord.app_commands import CommandTree, default_permissions
from util.resources import TOKEN
from util.functions import log 
from os import listdir
from os.path import isfile, join

class aclient(Client):
    def __init__(self):
        super().__init__(intents=Intents.default())
        self.synced = False
        self.commands = {}
        self.context_menus = {}
    
    async def on_ready(self):
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Logged in as {self.user}.")
        await client.change_presence(activity=Game(name="with command blocks"))
        tree.togetherControl = await DiscordTogether(TOKEN)
        channel = client.get_channel(1100118723072897055)
        #channel = client.get_channel(1040593202060730519)
        embed = Embed(title=" ",description=f"**``{self.user}, has appeared.``\nPing: {round (client.latency * 1000)} ms**")
        log(f"(SUCCESS) {self.user} has been STARTED. Ping: {round (client.latency * 1000)} ms")
        await channel.send(" ", embed=embed)

client = aclient()
tree = CommandTree(client)

# Read each command in commands folder
for command in listdir("commands"):
    if (not(isfile(join("commands", command)))):
        continue
            
    # Command
    module = __import__("commands." + command[:-3], fromlist=["commandFunction"])  # Retirez l'extension .py
    commandObject = client.commands[command] = globals()[module.__name__] = module
    #CommandObject contains all informations to add command to discord
    commandObject.commandFunction(tree, client)

# RSame thing for context menu
for command in listdir("context_menu"):
    if (not(isfile(join("context_menu", command)))):
        continue
            
    # Command
    module = __import__("context_menu." + command[:-3], fromlist=["commandFunction"])  # Retirez l'extension .py
    commandObject = client.context_menus[command] = globals()[module.__name__] = module
    #CommandObject contains all informations to add command to discord
    commandObject.commandFunction(tree, client)


client.run(TOKEN)