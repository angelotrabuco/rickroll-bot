import discord, os, json, tokens
from discord.ext import commands
Client = discord.Client()

client = commands.Bot(
                    command_prefix=commands.when_mentioned,
                    status=discord.Status.dnd,
                    activity=discord.Activity(type=discord.ActivityType.watching, name='rickroll.com'),
                    description="We're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\n\nI just wanna tell you how I'm feeling\nGotta make you understand",
                    case_insensitive=True,
                    allowed_mentions=discord.AllowedMentions.none(),
                    intents=discord.Intents.default()
                    )

client.load_extension('jishaku')
client.load_extension('rickroll')
client.rickroll = {}

client.run(tokens.bot)
