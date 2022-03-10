import asyncio

import discord
from discord.ext import commands

from src.RoleManager.RoleButton import RoleButton
from src.TimestampGenerator import TimestampGenerator

ts = TimestampGenerator("ROLE")


class RoleManagerCog(commands.Cog):
    guild: discord.Guild

    def __init__(self, bot):
        self.bot = bot
        self.guild = self.bot.guild
        print(ts.get_time_stamp(), "Starting Role Manager")
        asyncio.get_event_loop().create_task(self.create_role_buttons(False))

    async def create_role_buttons(self, send_new):

        pronoun_view = discord.ui.View(timeout=None)
        for role in self.bot.pronounDict:
            pronoun_view.add_item(RoleButton(role, style=discord.ButtonStyle.green))

        in_game_view = discord.ui.View(timeout=None)
        in_game_view.add_item(RoleButton(self.bot.roleDict["In-Game Leader"]))
        in_game_view.add_item(RoleButton(self.bot.roleDict["AWPer"]))
        in_game_view.add_item(RoleButton(self.bot.roleDict["Lurker"]))
        in_game_view.add_item(RoleButton(self.bot.roleDict["Support"]))
        in_game_view.add_item(RoleButton(self.bot.roleDict["Entry Fragger"]))

        rank_view = discord.ui.View(timeout=None)
        rank_view.add_item(RoleButton(self.bot.roleDict["Silver"], style=discord.ButtonStyle.red))
        rank_view.add_item(RoleButton(self.bot.roleDict["Gold Nova"], style=discord.ButtonStyle.red))
        rank_view.add_item(RoleButton(self.bot.roleDict["Master Guardian"], style=discord.ButtonStyle.red))
        rank_view.add_item(RoleButton(self.bot.roleDict["Legendary Eagle"], style=discord.ButtonStyle.red))
        rank_view.add_item(RoleButton(self.bot.roleDict["Global Elite"], style=discord.ButtonStyle.red))

        major_view = discord.ui.View(timeout=None)
        for role in self.bot.majorDict:
            major_view.add_item(RoleButton(role, style=discord.ButtonStyle.gray))

        grade_view = discord.ui.View(timeout=None)
        for role in self.bot.gradeDict:
            grade_view.add_item(RoleButton(role, style=discord.ButtonStyle.green))

        if send_new:
            await self.bot.channelDict["roles"].send("**Pronouns (You can select multiple)**", view=pronoun_view)
            await self.bot.channelDict["roles"].send("**In-Game Role**", view=in_game_view)
            await self.bot.channelDict["roles"].send("**In-Game Rank**", view=rank_view)
            await self.bot.channelDict["roles"].send("**Major**", view=major_view)
            await self.bot.channelDict["roles"].send("**Year**", view=grade_view)
        else:
            self.bot.add_view(pronoun_view)
            self.bot.add_view(in_game_view)
            self.bot.add_view(rank_view)
            self.bot.add_view(major_view)
