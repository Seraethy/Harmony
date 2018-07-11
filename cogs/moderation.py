import datetime
import discord

from discord.ext import commands


MUTED_ROLE = 446371354615218186


class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f"{argument} is not a valid member or member ID.") from None
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
            raise commands.BadArgument("Not a valid previously-banned member.")
        return entity


class Moderation:

    def __init__(self, bot):
        self.bot = bot
        self.timers = bot.get_cog("Timers")
        self.stafflog = bot.get_cog("Stafflog")
        
    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Helper")
    async def kick(self, ctx, member: MemberID, *, reason=None):
        if reason is None:
            reason = "The author didn't provide a reason"
        if ctx:
            try:
                user = await self.bot.get_user_info(member)
                em = discord.Embed(description=f"{user} got kicked!")
                em.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed=em, delete_after=6)
                emb = discord.Embed(description=f"Action: Kick\nReason: {reason}")
                emb.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await user.send(embed=emb)
                await ctx.guild.kick(discord.Object(id=member), reason=reason)
            except Exception:
                await ctx.guild.kick(discord.Object(id=member), reason=reason)
        await self.stafflog.make_case(member, "Kick", reason, ctx.author)

    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Helper")
    async def ban(self, ctx, member: MemberID, *, reason=None):
        if reason is None:
            reason = "The author didn't provide a reason"
        if ctx:
            try:
                user = await self.bot.get_user_info(member)
                em = discord.Embed(description=f"{user} got banned!")
                em.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed=em, delete_after=6)
                if user in ctx.guild.members:
                    emb = discord.Embed(description=f"Action: Ban\nReason: {reason}")
                    emb.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                    await user.send(embed=emb)
                    await ctx.guild.ban(discord.Object(id=member), reason=reason)
                else:
                    await ctx.guild.ban(discord.Object(id=member), reason=reason)
            except Exception:
                await ctx.guild.ban(discord.Object(id=member), reason=reason)
        await self.stafflog.make_case(member, "Ban", reason, ctx.author)

    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Helper")
    async def softban(self, ctx, member: MemberID, *, reason=None):
        if reason is None:
            reason = "The author didn't provide a reason"
        if ctx:
            try:
                user = await self.bot.get_user_info(member)
                em = discord.Embed(description=f"{user} got softbanned!")
                em.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed=em, delete_after=6)
                if user in ctx.guild.members:
                    emb = discord.Embed(description=f"Action: Softban\nReason: {reason}")
                    emb.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                    await user.send(embed=emb)
                    await ctx.guild.ban(discord.Object(id=member), reason=reason)
                    await ctx.guild.unban(discord.Object(id=member), reason=reason)
                else:
                    await ctx.guild.ban(discord.Object(id=member), reason=reason)
                    await ctx.guild.unban(discord.Object(id=member), reason=reason)
            except Exception:
                await ctx.guild.ban(discord.Object(id=member), reason=reason)
                await ctx.guild.unban(discord.Object(id=member), reason=reason)
        await self.stafflog.make_case(member, "Softban", reason, ctx.author)

    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Helper")
    async def unban(self, ctx, member: BannedMember, *, reason=None):
        if reason is None:
            reason = "The author didn't provide a reason"
        em = discord.Embed(description=f"{member.user} got their ban removed!")
        em.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed=em, delete_after=6)
        await ctx.guild.unban(member.user, reason=reason)
        await self.stafflog.make_case(member, "Unban", reason, ctx.author)

    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Helper")
    async def mute(self, ctx, member: discord.Member, minutes: int = 5, *, reason=None):
        if reason is None:
            reason = "The author didn't provide a reason"
        if ctx:
            try:
                em = discord.Embed(description=f"{member} got muted!")
                em.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed=em, delete_after=6)
                emb = discord.Embed(description=f'Mute ({minutes} minute{"s" if minutes!=1 else ""})\nReason: {reason}')
                emb.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await member.send(embed=emb)
                await member.add_roles(discord.utils.get(ctx.guild.roles, id=MUTED_ROLE))
            except Exception:
                await member.add_roles(discord.utils.get(ctx.guild.roles, id=MUTED_ROLE))
        await self.timers.create_timer("unmute", datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes), [ctx.guild.id, member.id])
        await self.stafflog.make_case(member, f'Mute ({minutes} minute{"s" if minutes!=1 else ""})', reason, ctx.author)
    
    async def on_unmute_event(self, guild_id, user_id):
        guild = self.bot.get_guild(guild_id)
        member = guild.get_member(user_id)
        if member:
            try:
                await member.remove_roles(discord.utils.get(guild.roles, id=MUTED_ROLE))
            except Exception:
                return

    @commands.command()
    @commands.has_any_role("Administrator", "Moderator", "Helper")
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        if reason is None:
            reason = "The author didn't provide a reason"
        if ctx:
            try:
                em = discord.Embed(description=f"{member} got their mute removed!")
                em.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await ctx.send(embed=em, delete_after=6)
                emb = discord.Embed(description=f"Unmute\nReason: {reason}")
                emb.set_author(name=f"{ctx.author} ({ctx.author.id})", icon_url=f"{ctx.author.avatar_url}")
                await member.send(embed=emb)
                await member.remove_roles(discord.utils.get(ctx.guild.roles, id=MUTED_ROLE))
            except Exception:
                await member.remove_roles(discord.utils.get(ctx.guild.roles, id=MUTED_ROLE))
        await self.stafflog.make_case(member, "Unmute", reason, ctx.author)


#ADD CLEAR/PRUNE COMMAND
#CLEAN UP THE CODE EVENTUALLY
#ADD A WARN COMMAND
#MAYBE ADD INVOCATION DELETION (ctx.message.delete())
#A TEMPORARY BAN WITH TIMER AND SHIT
#MAKE IT SO YOU CAN'T USE COMMANDS ON OTHER STAFF

def setup(bot):
    bot.add_cog(Moderation(bot))