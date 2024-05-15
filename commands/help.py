from discord import Interaction, Embed, ButtonStyle 
from discord.app_commands import ContextMenu, CommandTree, allowed_contexts, allowed_installs, AppCommand
from discord.ui import Button, View
from util.functions import log, logUser

commandsDetails:object = {}

def commandFunction(tree:CommandTree, client):
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    @tree.command(name="help",description="Show all the commands")
    async def helpCommand(interaction: Interaction):
        logUser(interaction.user.id)
        if len(commandsDetails) <= 0:
            #D Give an array of all commands
            commands:list[AppCommand] = await tree.fetch_commands()
            if commands == None:
                commands = tree.get_commands()
            for elt in commands:
                if isinstance(elt, ContextMenu):
                    continue

                id:int = 0
                description:str = ""
                try:
                    id = elt.id
                    description = elt.description
                except AttributeError:
                    id = id
                    description = description
                
                commandsDetails[elt.name] = {"description": elt.description, "id": id}

        generalCommandList = ["hello", "ping", "credits", "status", "youtube", "vote", "random"]
        moderationCommandList = [ "ban", "kick", "say", "timeout", "unmute", "role"]
        minecraftCommandList = ["modrinth", "skyblock", "player", "watchdog"]

        def getFieldContentCommand(name:str):
            response:list = [f"/{name}", "", False]

            command = commandsDetails[name]
            if not(command == None): 
                id:int = 0
                description:str = ""
                try:
                    id = command['id']
                    description = command['description']
                except AttributeError:
                    id = id
                    description = description
                
                response = [f"</{name}:{id}>", f"\n{description}", False]
            return response

        def addFieldToEmbed(embed, commandList): 
            for commandName in commandList:
                commandAttribute:list = getFieldContentCommand(commandName)
                embed.add_field(name=commandAttribute[0], value=commandAttribute[1], inline=commandAttribute[2])


        embed = Embed(title="Bot commands",description="")
        embed.add_field(name="\n__General__", value="", inline=False)
        addFieldToEmbed(embed, generalCommandList)

        embed.add_field(name="\n__Moderation__", value="", inline=False)
        addFieldToEmbed(embed, moderationCommandList)

        embed.add_field(name="\n__Minecraft__", value="", inline=False)
        addFieldToEmbed(embed, minecraftCommandList)

        button = Button(label='Vote for the bot on top.gg', style=ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
        button2 = Button(label='Invite the bot on your server', style=ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
        view = View()
        view.add_item(button)
        view.add_item(button2)
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /help")
