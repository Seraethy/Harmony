import discord


class Join:

    
    def __init__(self, bot):
        self.bot = bot

    
    async def on_member_join(self, member):
        if member:
            try:
                em = discord.Embed(description='')
                em.set_author(name='Harmony#8978 (447420402713755648)', icon_url='https://cdn.discordapp.com/avatars/447420402713755648/48936083e9e75a45912a1550909913e7.png?size=2048')
                await member.send(embed=em)
            except:
                pass

        ch = self.bot.get_channel(428929346359525386)
        await ch.send('')
        await member.add_roles(discord.utils.get(member.guild.roles, id=437972738473197568))
        await member.add_roles(discord.utils.get(member.guild.roles, id=451747441734189067))


def setup(bot):
    bot.add_cog(Join(bot))