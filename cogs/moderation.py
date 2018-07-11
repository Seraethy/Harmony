import datetime
import discord

from discord.ext import commands


class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f'{argument} is not a valid member or member ID.') from None
        else:
            can_execute = ctx.author.id == ctx.bot.owner_id or \
                          ctx.author == ctx.guild.owner or \
                          ctx.author.top_role > m.top_role

            if not can_execute:
                raise commands.BadArgument('You cannot do this action on this user due to role hierarchy.')
            return m.id


class BannedMember(commands.Converter):
    async def convert(self, ctx, argument):
        ban_list = await ctx.guild.bans()
        try:
            member_id = int(argument, base=10)
            entity = discord.utils.find(lambda u: u.user.id == member_id, ban_list)
        except ValueError:
            entity = discord.utils.find(lambda u: str(u.user) == argument, ban_list)

        if entity is None:
            raise commands.BadArgument('Not a valid previously-banned member.')
        return entity


class Moderation:


    def __init__(self, bot):
        self.bot = bot
        self.stafflog = bot.get_cog('Stafflog')
        self.timers = bot.get_cog('Timers')


    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if discord.utils.get(member.roles, id=437969862573424670):
            em = discord.Embed(description='You can\'t kick a staff member')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=em, delete_after=6)
            return

        elif reason is None:
            reason = 'The author didn\'t provide a reason'
        
        elif ctx: 
            try:
                emb = discord.Embed(description=f'{member} got kicked')
                emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=emb, delete_after=6)
                embe = discord.Embed(description=f'Action: Kick\nReason: {reason}')
                embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await member.send(embed=embe)
            except:
                pass

        await ctx.guild.kick(discord.Object(id=member.id), reason=reason)
        await self.stafflog.make_case(member, "Kick", reason, ctx.author)


    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def ban(self, ctx, member: MemberID, *, reason=None):
        server = self.bot.get_guild(406872145692590080)
        user = server.get_member(member)
        if discord.utils.get(user.roles, id=437969862573424670):
            em = discord.Embed(description='You can\'t ban a staff member')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=em, delete_after=6)
            return
        
        elif reason is None:
            reason = 'The author didn\'t provide a reason'

        elif ctx:
            try:
                emb = discord.Embed(description=f'{user} got banned')
                emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=emb, delete_after=6)
                embe = discord.Embed(description=f'Action: Ban\nReason: {reason}')
                embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await user.send(embed=embe)
            except:
                pass

        await ctx.guild.ban(discord.Object(id=member), reason=reason)
        await self.stafflog.make_case(user, 'Ban', reason, ctx.author)


    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def tempban(self, ctx, member: MemberID, days: int, *, reason=None):
        server = self.bot.get_guild(406872145692590080)
        user = server.get_member(member)
        if discord.utils.get(user.roles, id=437969862573424670):
            em = discord.Embed(description='You can\'t ban a staff member')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=em, delete_after=6)
            return

        elif reason is None:
            reason = 'The author didn\'t provide a reason'

        elif ctx:
            try:
                emb = discord.Embed(description=f'{user} got banned for {days} day{"s" if days!=1 else ""}')
                emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=emb, delete_after=6)
                embe = discord.Embed(description=f'Action: Temporary ban ({days} day{"s" if days!=1 else ""})\nReason: {reason}')
                embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await user.send(embed=embe)                
            except:
                pass

        await ctx.guild.ban(discord.Object(id=member), reason=reason)
        await self.timers.create_timer('unban', datetime.datetime.utcnow() + datetime.timedelta(days=days), [ctx.guild.id, member])
        await self.stafflog.make_case(user, f'Temporary ban ({days} day{"s" if days!=1 else ""})', reason, ctx.author)


    async def on_unban_event(self, guild_id, user_id):
        guild = self.bot.get_guild(guild_id)
        member = guild.get_member(user_id)
        if member:
            try:
                await guild.unban(discord.Object(id=member.id), reason='Expiration of temporary ban')
                await self.stafflog.make_case(member, 'Unban', 'Expiration of temporary ban', 'Harmony#8978')
            except:
                return


    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def softban(self, ctx, member: MemberID, *, reason=None):
        server = self.bot.get_guild(406872145692590080)
        user = server.get_member(member)
        if discord.utils.get(user.roles, id=437969862573424670):
            em = discord.Embed(description='You can\'t ban a staff member')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=em, delete_after=6)
            return

        elif reason is None:
            reason = 'The author didn\'t provide a reason'

        elif ctx:
            try:
                emb = discord.Embed(description=f'{user} got softbanned')
                emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=emb, delete_after=6)
                embe = discord.Embed(description=f'Action: Softban\nReason: {reason}')
                embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await user.send(embed=embe)                
            except:
                pass

            await ctx.guild.ban(discord.Object(id=member), reason=reason)
            await ctx.guild.unban(discord.Object(id=member), reason=reason)
            await self.stafflog.make_case(member, 'Softban', reason, ctx.author)
        

    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def unban(self, ctx, member: BannedMember, *, reason=None):
        if reason is None:
            reason = 'The author didn\'t provide a reason'

        elif ctx:
            try:
                emb = discord.Embed(description=f'{member.user} got their ban removed')
                emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=emb, delete_after=6)              
            except:
                pass

        await ctx.guild.unban(member.user, reason=reason)
        await self.stafflog.make_case(member.user, 'Unban', reason, ctx.author)


    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def mute(self, ctx, member: discord.Member, minutes: int, *, reason=None):
        if discord.utils.get(member.roles, id=437969862573424670):
            em = discord.Embed(description='You can\'t mute a staff member')
            em.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=em, delete_after=6)
            return
        
        elif discord.utils.get(member.roles, id=446371354615218186):
            emb = discord.Embed(description='You can\'t mute a member twice')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=emb, delete_after=6)
            return

        elif reason is None:
            reason = 'The author didn\'t provide a reason'

        elif ctx:
            try:
                embe = discord.Embed(description=f'{member} got muted')
                embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=embe, delete_after=6)
                embed = discord.Embed(description=f'Action: Mute ({minutes} minute{"s" if minutes!=1 else ""})\nReason: {reason}')
                embed.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await member.send(embed=embed)
            except:
                pass
        
        await member.add_roles(discord.utils.get(ctx.guild.roles, id=446371354615218186))        
        await self.timers.create_timer('unmute', datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes), [ctx.guild.id, member.id])
        await self.stafflog.make_case(member, f'Mute ({minutes} minute{"s" if minutes!=1 else ""})', reason, ctx.author)


    async def on_unmute_event(self, guild_id, user_id):
        guild = self.bot.get_guild(guild_id)
        member = guild.get_member(user_id)
        if member:
            try:
                try:
                    em = discord.Embed(description='Action: Unmute\nReason: Expiration of mute')
                    em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                    await member.send(embed=em)
                except:
                    pass
                await member.remove_roles(discord.utils.get(guild.roles, id=446371354615218186))
                await self.stafflog.make_case(member, 'Unmute', 'Expiration of mute', 'Harmony#8978')
            except:
                return


    @commands.command()
    @commands.has_any_role('Administrator', 'Moderator', 'Helper')
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        if discord.utils.get(member.roles, id=446371354615218186) is None:
            em = discord.Embed(description='This person isn\'t muted')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=em, delete_after=6)
            return

        elif reason is None:
            reason = 'The author didn\'t provide a reason'

        elif ctx:
            try:
                emb = discord.Embed(description=f'{member} got their mute removed')
                emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=emb, delete_after=6)
                embe = discord.Embed(description=f'Action: Unmute\nReason: {reason}')
                embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
                await member.send(embed=embe)
            except:
                pass

        await member.remove_roles(discord.utils.get(ctx.guild.roles, id=446371354615218186))
        await self.stafflog.make_case(member, 'Unmute', reason, ctx.author)


def setup(bot):
    bot.add_cog(Moderation(bot))

#COLOR EMBEDS?
#CLEAR/PRUNE COMMANDS
#WARN COMMANDS