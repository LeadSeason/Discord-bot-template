from discord.ext import commands
import discord

# cog template


class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def template(self, ctx):
        await ctx.send("aaaaaaaaaaaaaaaaaa")

    @commands.command()
    async def embed_template(self, ctx):
        embed = discord.Embed(title="title", description="description")
        embed.add_field(name="name", value="value", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(template(bot))
