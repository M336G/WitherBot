from datetime import date, datetime
from json import dump
from util.resources import users
from discord import Member, Interaction, Embed, Role

async def permissionCheck(target:Member | Role, interaction:Interaction, response:str, log_str:str) -> bool:
    fail = not hasPermission(interaction.user, target)
    if fail:
            await interaction.response.send_message(embed=Embed(description=response, colour=15548997))
            log(log_str)
    return fail

def hasPermission(user:Member, target:Member | Role) -> bool:
    if isinstance(target, Role):
         return (user.guild.owner_id == user.id or user.top_role.position > target.position)
    else:
        return (user.guild.owner_id == user.id or user.top_role.position > target.top_role.position) and not target.guild_permissions.administrator
def log(text: str):
    f = open("logs.txt", "a")
    f.write(f"[{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M:%S')}] {text}\n")
    f.close()
    return

def logUser(user_id: int):
    if user_id not in users:
        users.append(user_id)
        with open("data.json", "w") as dataFile:
            dump({"users": users}, dataFile, indent=4)
        log(f"(INFO) New unique user! ({user_id})")
    return