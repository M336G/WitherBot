from discord import Interaction, Embed, Member, Role, ButtonStyle
from discord.app_commands import default_permissions
from discord.ui import Button, View
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name="help",description="Show all the commands")
    async def helpCommand(interaction: Interaction):
        
        #D Give an array of all commands
        commands:[] = tree.get_commands()
        commandsDetails:object = {}
        for elt in commands:
            commandsDetails[elt.name] = elt.description

        embed = Embed(title="Bot commands",description="")
        embed.add_field(name="\n__General__", value="", inline=False)
        embed.add_field(name="\n/hello", value=f"\n{commandsDetails["hello"]}", inline=False)
        embed.add_field(name="\n/ping", value=f"\n{commandsDetails["ping"]}", inline=False)
        embed.add_field(name="\n/credits", value=f"\n{commandsDetails["credits"]}", inline=False)
        embed.add_field(name="\n/youtube", value=f"\n{commandsDetails["youtube"]}", inline=False)
        embed.add_field(name="\n/invite", value=f"\n{commandsDetails["invite"]}", inline=False)
        embed.add_field(name="\n/vote", value=f"\n{commandsDetails["vote"]}\n", inline=False)

        embed.add_field(name="\n__Moderation__", value="", inline=False)
        embed.add_field(name="\n/ban", value=f"\n{commandsDetails["ban"]}", inline=False)
        embed.add_field(name="\n/kick", value=f"\n{commandsDetails["kick"]}", inline=False)
        embed.add_field(name="\n/say", value=f"\n{commandsDetails["say"]}", inline=False)
        embed.add_field(name="\n/addrole", value=f"\n{commandsDetails["addrole"]}", inline=False)
        embed.add_field(name="\n/removerole", value=f"\n{commandsDetails["removerole"]}", inline=False)
        embed.add_field(name="\n/timeout", value=f"\n{commandsDetails["timeout"]}", inline=False)
        embed.add_field(name="\n/unmute", value=f"\n{commandsDetails["unmute"]}\n", inline=False)

        embed.add_field(name="\n__Hypixel / Skyblock__", value="", inline=False)
        embed.add_field(name="\n/skyblock_ehp", value=f"\n{commandsDetails["skyblock_ehp"]}", inline=False)
        embed.add_field(name="\n/skyblock_damage_reduction", value=f"\n{commandsDetails["skyblock_damage_reduction"]}", inline=False)
        embed.add_field(name="\n/skyblock_true_damage_reduction", value=f"\n{commandsDetails["skyblock_true_damage_reduction"]}", inline=False)
        embed.add_field(name="\n/skyblock_base_mana_regeneration", value=f"\n{commandsDetails["skyblock_base_mana_regeneration"]}", inline=False)
        embed.add_field(name="\n/skyblock_base_hp_regeneration", value=f"\n{commandsDetails["skyblock_base_hp_regeneration"]}", inline=False)
        embed.add_field(name="\n/skyblock_dungeons_requirement", value=f"\n{commandsDetails["skyblock_dungeons_requirement"]}", inline=False)
        embed.add_field(name="\n/skyblock_random_item", value=f"\n{commandsDetails["skyblock_random_item"]}", inline=False)

        embed2 = Embed(title=" ",description="")
        embed2.add_field(name="\n/player", value=f"\n{commandsDetails["player"]}", inline=False)
        embed2.add_field(name="\n/watchdog", value=f"\n{commandsDetails["watchdog"]}\n", inline=False)
        embed2.add_field(name="\n__Minecraft__", value="", inline=False)
        embed2.add_field(name="\n/modrinth", value=f"\n{commandsDetails["modrinth"]}", inline=False)
        embed2.add_field(name="\n/minecraft_random_item", value=f"\n{commandsDetails["minecraft_random_item"]}", inline=False)
        embed2.add_field(name="\n/minecraft_random_block", value=f"\n{commandsDetails["minecraft_random_block"]}", inline=False)

        button = Button(label='Vote for the bot on top.gg', style=ButtonStyle.url, url='https://top.gg/bot/1039238934682665030/vote')
        button2 = Button(label='Invite the bot on your server', style=ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1039238934682665030&permissions=1099780130822&scope=bot')
        view = View()
        view.add_item(button)
        view.add_item(button2)
        await interaction.response.send_message(" ",embed=embed)
        await interaction.channel.send(" ",embed=embed2, view=view)

        log(f"(SUCCESS) {interaction.user} used /help")
