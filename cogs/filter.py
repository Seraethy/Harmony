import datetime
import discord
import re


INVITE_REGEX = '(https?:\/\/)?(www\.)?(discord\.(gg|io|me|li)|discordapp\.com\/invite)\/.+'
LINK_REGEX = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
EXCLUDED_CHANNELS = []
EXCLUDED_CHANNELS_INVITE = []
EXCLUDED_CHANNELS_LINK = []
EXCLUDED_CHANNELS_ATTACHMENTS = []


class Filter:


    def __init__(self, bot):
        self.bot = bot
        self.stafflog = bot.get_cog('Stafflog')
        self.inviteregex = re.compile(INVITE_REGEX)
        self.linkregex = re.compile(LINK_REGEX)

    
    async def on_member_join(self, member):
        if member.created_at > datetime.datetime.now() - datetime.timedelta(days=1):
            try:
                em = discord.Embed(description='Action: Kick\nReason: Suspicion of spam/alt account')
                em.set_author(name=f'Harmony#8978 (447420402713755648)', icon_url=f'https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                await member.send(embed=em)
            except:
                pass
        
        await member.kick(reason='Suspicion of spam/alt account')
        await self.stafflog.make_case(member, 'Kick', 'Suspicion of spam/alt account', 'Harmony#8978')

    
    async def on_message(self, msg):
        if msg.guild is None:
            return
        
        elif msg.channel.id in EXCLUDED_CHANNELS:
            return

        if msg.author.bot:
            return

        invite = self.inviteregex.search(msg.content)
        if invite:
            if msg.channel.id in EXCLUDED_CHANNELS_INVITE:
                return

            elif discord.utils.get(msg.author.roles, id=437969862573424670) is None:
                try:
                    em = discord.Embed(description=f'{msg.author} got banned!')
                    em.set_author(name=f'Harmony#8978 (447420402713755648)', icon_url=f'https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                    await msg.channel.send(embed=em, delete_after=6)
                    emb = discord.Embed(description=f'Action: Ban\nReason: Advertising another server')
                    emb.set_author(name=f'Harmony#8978 (447420402713755648)', icon_url=f'https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                    await msg.author.send(embed=emb)
                except:
                    pass
            
            await msg.guild.ban(discord.Object(id=msg.author.id), reason='Advertising another server')
            await self.stafflog.make_case(msg.author, 'Ban', 'Advertising another server', 'Harmony#8978')

        link = self.linkregex.search(msg.content)
        if link:
            if msg.channel.id in EXCLUDED_CHANNELS_LINK:
                return
            
            elif discord.utils.get(msg.author.roles, id=451747449560629258) is None:
                await msg.delete()
                embe = discord.Embed(description=f'You need to be level 5 to post links')
                embe.set_author(name=f'Harmony#8978 (447420402713755648)', icon_url=f'https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                await msg.channel.send(embed=embe, delete_after=6)
                #LOG THE DELETED LINKS?

        if msg.attachments:
            if msg.channel.id in EXCLUDED_CHANNELS_ATTACHMENTS:
                return

            elif discord.utils.get(msg.author.roles, id=451747449560629258) is None:
                await msg.delete()
                embed = discord.Embed(description=f'You need to be level 5 to post images')
                embed.set_author(name=f'Harmony#8978 (447420402713755648)', icon_url=f'https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                await msg.channel.send(embed=embed, delete_after=6)

        if len(msg.mentions) >= 10:
            try:
                await msg.delete()
                em = discord.Embed(description=f'{msg.author} got banned')
                em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                await msg.channel.send(embed=em, delete_after=6)
                emb = discord.Embed(description='Action: Ban\nReason: Mentioning more than 10 members')
                emb.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
            except:
                pass

            await msg.guild.ban(discord.Object(id=msg.author.id), reason='Mentioning more than 10 members')
            await self.stafflog.make_case(msg.author, 'Ban', 'Mentioning more than 10 members', 'Harmony#8978')

        if len(msg.mentions) >= 5:
            await msg.delete()
            em = discord.Embed(description='You aren\'t allowed to mention more than 5 people at once')
            em.set_author(name=f'Harmony#8978 (447420402713755648)', icon_url=f'https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
            await msg.channel.send(embed=em, delete_after=6)


def setup (bot):
    bot.add_cog(Filter(bot))