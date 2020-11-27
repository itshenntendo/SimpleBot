import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

bot_name = "" #Create your bots name.

@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="Pong 🏓", description="Ping has been returned.", color=0x00a3d8)
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)

bot.run('Bot Token)
