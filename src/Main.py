import discord
from discord.ext import commands

from src import active_guild_id
from src.EmojiRegistration.EmojiRegistrationCog import EmojiRegistrationCog
from src.PinSystem.PinCog import PinCog
from src.RoleManager.RoleManagerCog import RoleManagerCog
from src.TimestampGenerator import TimestampGenerator
from src.Translation.TranslationCog import TranslationCog
from src.WikiCurrentCog.WikiCurrentCog import WikiCurrentCog

ts = TimestampGenerator("BANE")


class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        self.guild = None
        self.channelDict = {}
        self.roleDict = {}
        self.majorDict = []
        self.pronounDict = []
        self.gradeDict = []
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        # Find guild that matches active_guild_id
        self.guild = [guild for guild in self.guilds if guild.id == active_guild_id][0]
        print(ts.get_time_stamp(), "Found Active Guild: " + self.guild.name)

        # Populate channelDict for future convenience
        for a in self.guild.text_channels:
            self.channelDict[a.name] = a

        for r in self.guild.roles:
            if r.color == discord.Color.from_rgb(149, 165, 166):
                self.majorDict.append(r)
            elif r.color == discord.Color.from_rgb(96, 125, 139):
                self.pronounDict.append(r)
            elif r.color == discord.Color.from_rgb(151, 151, 151):
                self.gradeDict.append(r)
            else:
                self.roleDict[r.name] = r

        self.pronounDict.reverse()
        self.majorDict.reverse()

        # Start cogs
        print(ts.get_time_stamp(), 'Starting Cogs')
        bot.add_cog(RoleManagerCog(self))


# Read API key from file
f = open("data/key.txt", "r")
key = f.read()

# Create and start Bane Bot
bot = Bot()
bot.run(key)
