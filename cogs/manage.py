import discord

from discord.ext import commands


class Manage:


    def __init__(self, bot):
        self.bot = bot


    async def __local_check(self, ctx):
        return ctx.author.id in [332560050088443909]


    @commands.group()
    async def manage(self, ctx):
        if ctx.invoked_subcommand is None:
            raise commands.CommandInvokeError

    
    @manage.command()
    async def username(self, ctx, *, name):
        await self.bot.user.edit(username=name)

    
    @manage.command()
    @commands.guild_only()
    async def nickname(self, ctx, *, name=None):
        await ctx.guild.me.edit(nick=name)

    
    @manage.command(hidden=True, aliases=['ava'])
    async def avatar(self, ctx, url=None):
        if url:
            async with self.bot.session.get(url) as resp:
                if resp.status == 200:
                    await self.bot.user.edit(avatar=await resp.read())
        
        else:
            if ctx.message.attachments:
                async with self.bot.session.get(ctx.message.attachments[0].url) as resp:
                    if resp.status == 200:
                        await self.bot.user.edit(avatar=await resp.read())
            
            else:
                await self.bot.user.edit(avatar=None)


    @manage.command()
    async def status(self, ctx, status = 'online'):
        await self.bot.change_presence(status=discord.Status[status])

    
    @manage.commands()
    async def playing(self, ctx, *, game=None):
        await self.bot.change_presence(activity=discord.Game(name=game))

    
    @manage.commands()
    async def streaming(self, ctx, *, name=None, url=None):
        await self.bot.change_presence(activity=discord.Streaming(name=name, url=url))
        #MAY GIVE AN ERROR WHEN YOU DON'T PROVIDE EITHER A REASON OR URL


    @manage.commands()
    async def listening(self, ctx, *, name=None):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))


    @manage.commands()
    async def watching(self, ctx, *, name=None):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
    

def setup(bot):
    bot.add_cog(Manage(bot))