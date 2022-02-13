import discord
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import Bot as client
import random
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
import asyncio
import json
import requests
import aiohttp
from aiohttp import ClientSession
from datetime import datetime
import akinator
from datetime import datetime
client.launch_time = datetime.utcnow()


languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]



intents = discord.Intents(typing=True, presences=True, guilds=True,
                          members=True, reactions=True, messages=True,
                          invites=True, bans=True)


client = commands.Bot(command_prefix='3', intents=intents)
client.remove_command('help')
dev = [706611524826824834]


##Events##



@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"Over Ebola Kingdom"))
    print('Logged in as')
    print(f'{client.user.name}')
    print(f'Bot-ID: {client.user.id}')
    print('------')



##Events##



##Help Command##

@client.command()
async def help(ctx):

    embed = discord.Embed(title='Help Command', color=0x000000)

    embed.add_field()

    await ctx.author.send(embed=embed)

##Help Command##
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title='Pong?', color=0x000000)
    m = await ctx.send(embed=embed)

    await asyncio.sleep(1)

    embed = discord.Embed(title='**My Connection**', description=f'My Ping Is {round(client.latency * 1000)}ms',
                          color=0x000000)
    await m.edit(embed=embed)



@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinfo(ctx):


	embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at, title="**Server Info.**")
	embed.add_field(name=f"**Name**", value=ctx.guild.name)
	embed.add_field(name=f"**ID**", value=ctx.guild.id, inline=False)
	embed.add_field(name=f"**Region**", value=ctx.guild.region, inline=False)
	embed.add_field(name=f"**Created On**", value=ctx.guild.created_at.strftime("%a, %B %#d %Y"), inline=False)
	embed.add_field(name=f"**Member Count**", value=len(ctx.guild.members), inline=True)
	embed.add_field(name=f"**Role Amount**", value=len(ctx.guild.roles), inline=True)
	embed.add_field(name=f'**Banned Members**', value=f'{len(await ctx.guild.bans())}', inline=True)
	embed.set_thumbnail(url=ctx.guild.icon_url)
	embed.set_footer(text=f"Requested By {ctx.author.display_name}")
	await ctx.send(embed=embed)


@client.command(aliases=['8ball'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes",
                 "Ask again later",
                 "Better not tell you now",
                 "Cannot predict now",
                 "Concentrate and ask again",
                 "Don’t count on it",
                 "It is certain",
                 "It is decidedly so",
                 "Most likely",
                 "My reply is no",
                 "My sources say no",
                 "Outlook good",
                 "Outlook not so good",
                 "Reply hazy try again",
                 "Signs point to yes",
                 "Very doubtful",
                 "Without a doubt",
                 "Yes",
                 "Yes, definitely",
                 "You may rely on it"]
    embed = discord.Embed(color=0x000000, title=f"8Ball")
    embed.add_field(name=f'**Question:**', value=(f"``{question}`` \n \n"
    	                                      f"**Answer**: \n"
    	                                      f"{random.choice(responses)}"))
    embed.set_thumbnail(url='https://www.vippng.com/png/full/0-3078_download-png-image-report-8-ball-icon-png.png')
    await ctx.send(embed=embed)

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Youre on cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hack(ctx, member: discord.Member = None):

    await ctx.send(f"ED Hacking {member.mention}..", delete_after=5)
    

    await asyncio.sleep(5)


    passwords =['imnothackedlmao','sendnoodles63','ilovenoodles','icantcode','christianmicraft','server','icantspell','hackedlmao','WOWTONIGHT','69', 'ilovefn123']
    fakeips =['154.2345.24.743','255.255.255.0','356.653.56','101.12.8.6053','255.255.255.0']


    embed = discord.Embed(title=f"{member.display_name} info ", description=f"Email `{member.display_name}@gmail.com` Password `{random.choice(passwords)}`  IP `{random.choice(fakeips)}`", color=0x000000)
    embed.set_footer(text="You've totally been hacked ")
    await ctx.send(embed=embed)


@hack.error
async def hack_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0xFF0000, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}hack <user>``")
        await ctx.send(embed=embed)




@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar(ctx, member: discord.Member = None):

	member = ctx.author if not member else member

	embed = discord.Embed(color=0x000000, title=f"**{member.display_name}'s avatar.**")
	embed.set_image(url=member.avatar_url)

	await ctx.send(embed=embed)


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Youre on cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def userinfo(ctx, member: discord.Member = None):
    embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at, title=f"UserInfo")

    member = ctx.author if not member else member


    roles = [role for role in member.roles if role != ctx.guild.default_role]



    embed.add_field(name=f"**User**", value=f"{member}", inline=False)
    embed.add_field(name=f"**User ID**", value=member.id, inline=False)
    embed.add_field(name=f"**Account Created On**", value=member.created_at.strftime("%a, %B %#d %Y "), inline=False)
    embed.add_field(name=f"**Joined Server On**", value=member.joined_at.strftime("%a, %B %#d %Y "), inline=False)
    embed.add_field(name=f"**Roles**", value=" ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name=f"**Status**", value=f"{str(member.status).title()}", inline=False)
    embed.add_field(name=f"**Playing**", value=member.activity, inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)


@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Youre on cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


apples = [813963134921736192, 748307396300111883, 827937580422004797, 710774588014985286, 785313367329603644,
              805454548797358110, 748720708422598706, 701504461973225496, 701516341307244635, 785517871593816105,
              751343367098597406, 702832917490958398, 796832988280520724, 701813936550576231, 792376007809564682,
              700037102506606653, 790139031333240852]

@client.command()
async def akin(ctx):
    if ctx.channel.id in apples:
        return
    aki = akinator.Akinator()

    q = aki.start_game()
    while aki.progression <= 80:
        await ctx.send(q)
        a = await client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        # this is just to make it less case sensitive!
        if a.content == "yep":
            a.content = "yes"
        elif a.content == "nop" or "nope":
            a.content == "no"
        elif a.content == "proly":
            a.content == "p"
        elif a.content == "proly not":
            a.content == "pn"
        if a.content == "b":
            try:
                q = aki.back()
            except akinator.CantGoBackAnyFurther:
                pass
        else:
            try:
                q = aki.answer(a.content)
            except akinator.InvalidAnswerError:
                pass
    aki.win()
    em = discord.Embed(title=f"It's {aki.first_guess['name']}",
                       description=f"({aki.first_guess['description']})! Was I correct?", color=ctx.author.color)
    em.set_thumbnail(url=aki.first_guess['absolute_picture_path'])
    await ctx.send(embed=em)
    correct = await client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    if correct.content.lower() == "yes" or correct.content.lower() == "y" or correct.content.lower() == "yep" or correct.content.lower() == "sure" or correct.content.lower() == "easy":
        await ctx.send("Easy")
    else:
        await ctx.send("Aint that bouta bitch")


@client.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)


@client.command()
@commands.has_role('not real')
async def nuke(ctx):

    channel = ctx.channel
    channel_position = channel.position

    new_channel = await channel.clone()
    await channel.delete()
    await new_channel.edit(position=channel_position, sync_permissions=True)
    await new_channel.send("https://tenor.com/view/nuke-press-the-button-bomb-them-nuke-them-cat-gif-16361990")

@nuke.error
async def nuke(ctx, error):
    if isinstance(error, commands.MissingRole, ):
        await ctx.send(f'you do not have the required role to use this command.')


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="<a:check:939742228513959946> Uptime",
                    value=f"{days} days {hours} hours {minutes} minutes and {seconds}s")
    await ctx.trigger_typing()
    await ctx.send(embed=embed)





# LEAGUE SHIT

@client.command()
async def opgg(ctx, *args):
    """Pull up op.gg for players"""
    url = 'http://na.op.gg/'

    if len(args) == 1:
        url += 'summoner/userName=' + args[0]
    elif len(args) > 1:
        url += 'multi/query=' + args[0]
        for i in range(1, len(args)):
            url += '%2C' + args[i]

    await ctx.send(url)

# TOKEN

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0x000000, title=f"**Command Not Found!**")
        await ctx.send(embed=embed)


client.run("OTM4NTUyNjQwNTkyMjgxNjgx.Yfr9Qg.1wcpojHjnZAP7k-QbM6qQ68IakU")
