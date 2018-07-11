import discord
import random

from discord.ext import commands


EXTRA_GIFs = [
    'https://cdn.discordapp.com/attachments/463105098155819019/466317105030103070/alone.gif',
    'https://cdn.discordapp.com/attachments/463105098155819019/466325892856021002/alone_2.gif',
    'https://cdn.discordapp.com/attachments/463105098155819019/466326105503301643/alone_3.gif',
    'https://cdn.discordapp.com/attachments/463105098155819019/466326371258466314/alone_4.gif',
    'https://cdn.discordapp.com/attachments/463105098155819019/466326579186892810/alone_5.gif'
]


class Fun:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def kiss(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466263454471421953/kiss.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466263442165202964/kiss_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466263446711828490/kiss_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466263451359248392/kiss_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265062978355211/kiss_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265068921683968/kiss_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265073870962688/kiss_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266573716324362/kiss_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266584542085130/kiss_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266595161800706/kiss_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266597892292618/kiss_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266598735347731/kiss_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266601424027655/kiss_13.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268472150851585/kiss_14.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268466286952458/kiss_15.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268462826913793/kiss_16.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268465846550538/kiss_17.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268477435412480/kiss_18.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466269121693220895/kiss_19.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466269378980085790/kiss_20.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466270759577190400/kiss_21.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272868301537280/kiss_22.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272872382332940/kiss_23.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272908717588480/kiss_24.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274720761905153/kiss_25.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274721999224863/kiss_26.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274725732024320/kiss_27.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274727716192265/kiss_28.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265072587767808/kiss_cheek.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266622559125515/kiss_cheek_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466267393719533578/kiss_cheek_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466270767936438282/kiss_cheek_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466271628201033738/kiss_cheek_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272900513792020/kiss_cheek_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272917425225739/kiss_cheek_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272886123003904/kiss_cheek_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272912215769088/kiss_cheek_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272902010896404/kiss_cheek_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466314610639765514/kiss_cheek_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466314612275544074/kiss_cheek_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466314617279217675/kiss_cheek_13.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272905186246672/kiss_forehead.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274727736901632/kiss_forehead_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466279314430885898/kiss_forehead_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466279323599503370/kiss_forehead_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466279322441875466/kiss_forehead_5.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description=f'**{ctx.author.name}**, that\'s just sad...')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description=f'**{member.name}**, you got a kiss from **{ctx.author.name}**!')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @kiss.command(name='cheek')
    @commands.guild_only()
    async def kiss_cheek(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466265072587767808/kiss_cheek.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266622559125515/kiss_cheek_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466267393719533578/kiss_cheek_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466270767936438282/kiss_cheek_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466271628201033738/kiss_cheek_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272900513792020/kiss_cheek_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272917425225739/kiss_cheek_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272886123003904/kiss_cheek_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272912215769088/kiss_cheek_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272902010896404/kiss_cheek_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466314610639765514/kiss_cheek_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466314612275544074/kiss_cheek_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466314617279217675/kiss_cheek_13.gif'
        ]
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description=f'**{ctx.author.name}**, that\'s just sad...')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description=f'**{member.name}**, you got a kiss from **{ctx.author.name}**!')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @kiss.command(name='forehead')
    @commands.guild_only()
    async def kiss_forehead(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466272905186246672/kiss_forehead.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274727736901632/kiss_forehead_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466279314430885898/kiss_forehead_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466279323599503370/kiss_forehead_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466279322441875466/kiss_forehead_5.gif'
        ]
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description=f'**{ctx.author.name}**, that\'s just sad...')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description=f'**{member.name}**, you got a kiss from **{ctx.author.name}**!')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @kiss.command(name='lips')
    @commands.guild_only()
    async def kiss_lips(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466263454471421953/kiss.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466263442165202964/kiss_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466263446711828490/kiss_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466263451359248392/kiss_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265062978355211/kiss_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265068921683968/kiss_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466265073870962688/kiss_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266573716324362/kiss_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266584542085130/kiss_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266595161800706/kiss_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266597892292618/kiss_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266598735347731/kiss_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466266601424027655/kiss_13.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268472150851585/kiss_14.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268466286952458/kiss_15.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268462826913793/kiss_16.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268465846550538/kiss_17.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466268477435412480/kiss_18.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466269121693220895/kiss_19.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466269378980085790/kiss_20.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466270759577190400/kiss_21.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272868301537280/kiss_22.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272872382332940/kiss_23.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466272908717588480/kiss_24.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274720761905153/kiss_25.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274721999224863/kiss_26.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274725732024320/kiss_27.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466274727716192265/kiss_28.gif'
        ]
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description=f'**{ctx.author.name}**, that\'s just sad...')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description=f'**{member.name}**, you got a kiss from **{ctx.author.name}**!')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466277539355033641/slap.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277471382405130/slap_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277485428998144/slap_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277535538348034/slap_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277484435079208/slap_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277486649671681/slap_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277573622497280/slap_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277524859650094/slap_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277575308607500/slap_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277509055381514/slap_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466278351972204546/slap_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277542484115476/slap_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277544665153546/slap_13.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466278457207291924/slap_14.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277547509022720/slap_15.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277550189182977/slap_16.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277548502810654/slap_17.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277528412356628/slap_18.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277549471825932/slap_19.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277549471825932/slap_19.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466278694088867841/slap_20.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466277575619248138/slap_21.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466330651285520385/hug.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330621497704448/hug_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330630058278923/hug_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330629609488394/hug_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330629877923840/hug_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330631538868238/hug_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330645430403073/hug_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330649809256450/hug_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330651256291338/hug_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466330651633778689/hug_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332450704982017/hug_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332457600417794/hug_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332463963308032/hug_13.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332478219485194/hug_14.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332478706155530/hug_15.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332465628315653/hug_16.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332478768939008/hug_17.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466333977230311434/hug_18.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332491603640320/hug_19.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466332484813193247/hug_20.gif',
            #21 IS GLITCHY
            'https://cdn.discordapp.com/attachments/463105098155819019/466334133430255637/hug_22.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466334166305341471/hug_23.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466334142536351757/hug_24.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466334166242426890/hug_25.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466334161964236800/hug_26.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466334156738265088/hug_27.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466334156411109376/hug_28.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466353216842498068/cuddle.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353144784355341/cuddle_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353149322592267/cuddle_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353157044437004/cuddle_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353152707395594/cuddle_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353163193024512/cuddle_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353216515211264/cuddle_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353196781273089/cuddle_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353218922741771/cuddle_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353174517907456/cuddle_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353203341164544/cuddle_11.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353199817949195/cuddle_12.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353183648776192/cuddle_13.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353185393475586/cuddle_14.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353218436464650/cuddle_15.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353211372994560/cuddle_16.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466353212790800394/cuddle_17.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466361768307064853/lick.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361576652406794/lick_2.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361610169221120/lick_3.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361581849149473/lick_4.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361597716201482/lick_5.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361609560915969/lick_6.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361596386476044/lick_7.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361598483628033/lick_8.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361610269753344/lick_9.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361607031619585/lick_10.gif',
            'https://cdn.discordapp.com/attachments/463105098155819019/466361602204106753/lick_11.gif'
        ]
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command(aliases=['suck'])
    @commands.guild_only()
    async def succ(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466366978924478464/succ.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466367724696633351/pat.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def poke(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466367729172217866/poke.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)

    @commands.command()
    @commands.guild_only()
    async def highfive(self, ctx, member: discord.Member):
        GIFs = [
            'https://cdn.discordapp.com/attachments/463105098155819019/466367770041253888/highfive.gif'
        ]   
        if discord.utils.get(ctx.author.roles, id=451747451251064843) is None:
            em = discord.Embed(description='You need to be level 10 to use this command!')
            em.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            em.colour = ctx.author.color
            await ctx.send(embed=em, delete_after=6)
        
        elif ctx.author == member:
            emb = discord.Embed(description='')
            emb.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            emb.set_image(url=random.choice(EXTRA_GIFs))
            emb.colour = ctx.author.color
            await ctx.send(embed=emb)

        else:
            embe = discord.Embed(description='')
            embe.set_author(name=f'{ctx.author} ({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
            embe.set_image(url=random.choice(GIFs))
            embe.colour = ctx.author.color
            await ctx.send(embed=embe)


#ADD A GLOBAL TIMER TO THE COMMANDS
#RANDOM SAD GIF
#MAKE IT SO THE MAIN EMBED ISN'T BLACK

def setup(bot):
    bot.add_cog(Fun(bot))