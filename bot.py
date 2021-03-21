from db_handler import DbHandler
import os
from discord import message
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

bot = commands.Bot(command_prefix='!')
db = DbHandler(HOST, USER, PASSWORD, DATABASE)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="add")
async def add_command(ctx, assignment_name, class_name, turn_in_date):
    author = ctx.message.author

    query = {
        "assignment_name": assignment_name,
        "class_name": class_name,
        "turn_in_date": turn_in_date,
        "author": author.id,
        "guild": ctx.message.guild.id,
    }

    db.add_assignment(query)

    await ctx.send(f"Προσθέσα το μάθημα σου φίλτατε/η, {author.mention}.")

bot.run(TOKEN)
