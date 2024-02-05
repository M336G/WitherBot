from discord.ui import Modal, TextInput
from discord import Embed, TextStyle, Interaction, Member
from datetime import timedelta 
from util.functions import log

class ban_form(Modal, title='Ban'):
    def __init__(self, member:Member):
        self.member = member
        super().__init__()
    input_0 = TextInput(label="Ban Reason",placeholder="'None' if no reasons are provided",style=TextStyle.long, required=False)
    async def on_submit(self, interaction: Interaction):
        try:
            if self.input_0.value == "":
                try:
                    embed = Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.ban(reason=self.input_0.value)
                embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{self.member}`` has been banned from the server!**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)

                log(f"(SUCCESS) {interaction.user} BANNED {self.member} on {interaction.user.guild} ({interaction.user.guild.id})")
                
            else:
                try:
                    embed = Embed(title=f"**You have been banned from ``{interaction.guild.name}``!**\n``Reason: {self.input_0.value}``",description="", colour=15548997)
                    await self.member.send(" ",embed=embed)
                except:
                    embed2 = Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997)
                await self.member.ban(reason=self.input_0.value)
                embed = Embed(title=" ",description=f"<:gregban:1039247298808520794> **``{self.member}`` has been banned from the server!**\n**``Reason: {self.input_0.value}``**", colour=5763719)
                await interaction.response.send_message(" ",embed=embed)

                log(f"(SUCCESS) {interaction.user} BANNED {self.member} on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
        
        except:
            embed = Embed(title=" ",description="<:x:1039888272761049179> **An error occurred**", colour=15548997)
            await interaction.response.send_message(" ",embed=embed)
            
            log(f"(FAIL) {interaction.user} failed to use the ban application")
