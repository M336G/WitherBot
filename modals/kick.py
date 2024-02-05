from discord.ui import Modal, TextInput
from discord import Embed, TextStyle, Interaction, Member
from util.functions import log

class kick_form(Modal, title='Kick'):
    def __init__(self, member:Member):
        self.member = member
        super().__init__()
    input_0 = TextInput(label="Kick Reason",placeholder="'None' if no reasons are provided",style=TextStyle.long, required=False)
    async def on_submit(self, interaction: Interaction):
        try:
            if self.input_0.value == "":
                try:
                    embed = Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.kick(reason=self.input_0.value)
                embed = Embed(title=" ",description=f"**``{self.member}`` has been kicked from the server!**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                log(f"(SUCCESS) {interaction.user} BANNED {self.member} on {interaction.user.guild} ({interaction.user.guild.id})")
                
            else:
                try:
                    embed = Embed(title=f"**You have been kicked from ``{interaction.guild.name}``!**\n``Reason: {self.input_0.value}``",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.kick(reason=self.input_0.value)
                embed = Embed(title=" ",description=f"**``{self.member}`` has been kicked from the server!**\n**``Reason: {self.input_0.value}``**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)
                log(f"(SUCCESS) {interaction.user} KICKED {self.member} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
        
        except:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            log(f"(FAIL) {interaction.user} failed to use the kick application")
