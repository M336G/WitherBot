from discord_together import DiscordTogether
from discord import Client, Intents, Game, Embed, AllowedMentions
from discord.app_commands import CommandTree
from util.resources import TOKEN
from util.functions import log 
from os import listdir
from os.path import isfile, join

class aclient(Client):
    def __init__(self):
        super().__init__(intents=Intents.default(), allowed_mentions=AllowedMentions(roles=True, users=True, everyone=False))
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
        channel = client.get_channel(1040593202060730519)
        embed = Embed(title=" ",description=f"**``{self.user}, has appeared.``\nPing: {round (client.latency * 1000)} ms**")
        log(f"(SUCCESS) {self.user} has been STARTED. Ping: {round (client.latency * 1000)} ms")
        await channel.send(" ", embed=embed)

client = aclient()
tree = CommandTree(client)

# Read each command in the commands folder
for command in listdir("commands"):
    if (not(isfile(join("commands", command)))):
        continue
            
    # Command
    module = __import__("commands." + command[:-3], fromlist=["commandFunction"])  # Remove the .py extension
    commandObject = client.commands[command] = globals()[module.__name__] = module
    # CommandObject contains all the informations to add the commands to Discord
    commandObject.commandFunction(tree, client)

# RSame thing for context menu
for command in listdir("context_menu"):
    if (not(isfile(join("context_menu", command)))):
        continue
            
    # Command
    module = __import__("context_menu." + command[:-3], fromlist=["commandFunction"])  # Remove the .py extension
    commandObject = client.context_menus[command] = globals()[module.__name__] = module
    # CommandObject contains all the informations to add the commands to Discord
    commandObject.commandFunction(tree, client)

client.run(TOKEN)
