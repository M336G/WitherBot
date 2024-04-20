from discord.ui import Modal, TextInput
from discord import Embed, TextStyle, Interaction, Member
from datetime import timedelta 
from util.functions import log

class timeout_form(Modal, title='Timeout'):
    def __init__(self, member:Member):
        self.member = member
        super().__init__()
    input_0 = TextInput(label="Timeout Reason",placeholder="'None' if no reasons are provided",style=TextStyle.long, required=False)
    input_1 = TextInput(label="Days",placeholder="How long will be the timeout (in days, maximum of 28 days)",style=TextStyle.short, required=False)
    input_2 = TextInput(label="Hours",placeholder="How long will be the timeout (in hours)",style=TextStyle.short, required=False)
    input_3 = TextInput(label="Minutes",placeholder="How long will be the timeout (in minutes)",style=TextStyle.short, required=False)
    input_4 = TextInput(label="Seconds",placeholder="How long will be the timeout (in seconds)",style=TextStyle.short, required=False)
    async def on_submit(self, interaction: Interaction):
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

        timedeltaTimeout = timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        try:
            if self.input_0.value == "":
                await self.member.timeout(timedeltaTimeout,reason=self.input_0.value)
                await interaction.response.send_message(" ",embed=Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{self.member.id}> **for {days}d {hours}h {minutes}m {seconds}s**", colour=2067276))
                log(f"(SUCCESS) {interaction.user} MUTED {self.member} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id})")
                try:
                    await self.member.send(" ",embed=Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**",description="", colour=15548997))
                except:
                    await interaction.channel.send(" ",embed=Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997))
            else:
                await self.member.timeout(timedeltaTimeout,reason=self.input_0.value)
                await interaction.response.send_message(" ",embed=Embed(title=" ",description=f":white_check_mark: **Successfully muted** <@{self.member.id}> **for {days}d {hours}h {minutes}m {seconds}s**\n``Reason: {self.input_0.value}``", colour=2067276))
                log(f"(SUCCESS) {interaction.user} MUTED {self.member} for {days}d {hours}h {minutes}m {seconds}s on {interaction.user.guild} ({interaction.user.guild.id}) and gave a reason")
                try:
                    await self.member.send(" ",embed=Embed(title=f"**You have been muted on ``{interaction.guild.name}`` for {days}d {hours}h {minutes}m {seconds}s!**\n``Reason: {self.input_0.value}``",description="", colour=15548997))
                except:
                    await interaction.channel.send(" ",embed=Embed(title=" ",description=":x: **An error occurred while sending the message to the user**", colour=15548997))
        except:
            await interaction.response.send_message(" ",embed=Embed(title=" ",description=":x: **An error occurred**", colour=15548997))
            log(f"(FAIL) {interaction.user} failed to use the timeout application")
            