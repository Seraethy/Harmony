import datetime
import discord

import parsedatetime as pdt

from cogs.utils import time
from discord.ext import commands


def get_date(text):
    cal = pdt.Calendar()
    time, res = cal.parseDT(text, datetime.datetime.utcnow())
    return time if res else None


class Bump:


    def __init__(self, bot):
        self.bot = bot
        self.timers = bot.get_cog('Timers')


    @commands.command()
    @commands.has_any_role('Bump')
    async def disboard(self, ctx, *, time_till_bump='1h 59m'):
        ch = self.bot.get_channel(450197951047008256)
        t = get_date(time_till_bump)
        if t:
            await ctx.message.delete()
            em = discord.Embed(description=f'Created a bump reminder for DISBOARD\n({t} UTC)', colour='')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ch.send(embed=em)
            await self.timers.create_timer('disboard', t)
        
        else:
            #EMBED?
            await ctx.send('Please supply a proper time format', delete_after=6)

    
    async def on_disboard_event(self):
        ch = self.bot.get_channel(450197951047008256)
        em = discord.Embed(description='The server can be bumped on DISBOARD\nClick [here](https://disboard.org/dashboard/servers) to go to the website\nYou can also bump the server by typing `!disboard bump`', colour='')
        em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
        await ch.send('<@&450418369477345301>', delete_after=1)
        await ch.send(embed=em)


    @commands.command()
    @commands.has_any_role('Bump')
    async def discord(self, ctx, *, time_till_bump='5h 59m'):
        ch = self.bot.get_channel(450197951047008256)
        t = get_date(time_till_bump)
        if t:
            await ctx.message.delete()
            em = discord.Embed(description=f'Created a bump reminder for Discord Me\n({t} UTC)', colour='')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ch.send(embed=em)
            await self.timers.create_timer('discord', t)
        
        else:
            #EMBED?
            await ctx.send('Please supply a proper time format', delete_after=6)

    
    async def on_discord_event(self):
        ch = self.bot.get_channel(450197951047008256)
        em = discord.Embed(description='The server can be bumped on Discord Me\nClick [here](https://discord.me/server/bump-servers/86509) to go to the website', colour='')
        em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
        await ch.send('<@&450418369477345301>', delete_after=1)
        await ch.send(embed=em) 


    @commands.command()
    @commands.has_any_role('Bump')
    async def discordserv(self, ctx, *, time_till_bump='6h 0m 10s'):
        ch = self.bot.get_channel(450197951047008256)
        t = get_date(time_till_bump)
        if t:
            await ctx.message.delete()
            await ch.send('Automatically bumping DiscordServ.com from now on')
            await ch.send(';;bump')
            await self.timers.create_timer('discordserv', t)
        
        else:
            #EMBED?
            await ctx.send('Please supply a proper time format', delete_after=6)

    
    async def on_discordserv_event(self):
        time_till_bump = '6h 0m 10s'
        t = get_date(time_till_bump)
        ch = self.bot.get_channel(450197951047008256)
        await ch.send(';;bump')
        await self.timers.create_timer('discordserv', t)


    @commands.command()
    @commands.has_any_role('Bump')
    async def dlm(self, ctx, *, time_till_bump='6h 0m 10s'):
        ch = self.bot.get_channel(450197951047008256)
        t = get_date(time_till_bump)
        if t:
            await ctx.message.delete()
            await ch.send('Automatically bumping DLM (DiscordList.me) from now on')
            await ch.send('dlm!bump')
            await self.timers.create_timer('dlm', t)
        
        else:
            #EMBED?
            await ctx.send('Please supply a proper time format', delete_after=6)

    
    async def on_dlm_event(self):
        time_till_bump = '6h 0m 10s'
        t = get_date(time_till_bump)
        ch = self.bot.get_channel(450197951047008256)
        await ch.send('dlm!bump')
        await self.timers.create_timer('dlm', t)

    
    @commands.command(aliases=['discord-server'])
    @commands.has_any_role('Bump')
    async def servermonotoring(self, ctx, *, time_till_bump='3h 59m'):
        ch = self.bot.get_channel(450197951047008256)
        t = get_date(time_till_bump)
        if t:
            await ctx.message.delete()
            em = discord.Embed(description=f'Created a bump reminder for discord-server.com\n({t} UTC)', colour='')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ch.send(embed=em)
            await self.timers.create_timer('discordmonotoring', t)
        
        else:
            #EMBED?
            await ctx.send('Please supply a proper time format', delete_after=6)

    
    async def on_discordmonotoring_event(self):
        ch = self.bot.get_channel(450197951047008256)
        em = discord.Embed(description='The server can be bumped on discord-server.com\nYou can bump the server by typing `!bump', colour='')
        em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
        await ch.send('<@&450418369477345301>', delete_after=1)
        await ch.send(embed=em) 


    @commands.command()
    @commands.has_any_role('Bump')
    async def serverhound(self, ctx, *, time_till_bump='3h 59m'):
        ch = self.bot.get_channel(450197951047008256)
        t = get_date(time_till_bump)
        if t:
            await ctx.message.delete()
            em = discord.Embed(description=f'Created a bump reminder for ServerHound\n({t} UTC)', colour='')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ch.send(embed=em)
            await self.timers.create_timer('serverhound', t)
        
        else:
            #EMBED?
            await ctx.send('Please supply a proper time format', delete_after=6)

    
    async def on_serverhound_event(self):
        ch = self.bot.get_channel(450197951047008256)
        em = discord.Embed(description='The server can be bumped on ServerHound\nYou can bump the server by typing `=bump', colour='')
        em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
        await ch.send('<@&450418369477345301>', delete_after=1)
        await ch.send(embed=em) 


def setup(bot):
    bot.add_cog(Bump(bot))


#ADD ALL OTHER WEBSITES IN THE FUTURE
#STILL NEED TO CHECK FOR MISTAKES