import discord
from discord.ext import commands
import sqlite3

class Level(commands.Cog, name="Level"):
    
    def __init__(self, bot):
        self.bot = bot

"""    
    @commands.command()
    async def init(self, ctx):
        con = sqlite3.connect('database/level.db')
        cur = con.cursor()
        
        cur.execute(f'''CREATE TABLE IF NOT EXISTS GUILD_{ctx.guild.id} (user_id int NOT NULL, exp int DEFAULT 0, lvl int DEFAULT 0) ''')
        for x in ctx.guild.members:
            if x.bot != True:
                cur.execute(f"INSERT INTO GUILD_{ctx.guild.id} (user_id) VALUES ({x.id})")
        con.commit()
        await ctx.channel.send("Leveling system initiaized")
            
    @commands.command()
    async def xp(self, ctx, user: discord.User = None):
        con = sqlite3.connect('database/level.db')
        cur = con.cursor()
        try:
            if user == None:
                cur.execute(f"SELECT * FROM GUILD_{ctx.guild.id} WHERE user_id={ctx.author.id}")
                result = cur.fetchone()
                await ctx.channel.send(f"{ctx.author.mention} Exp:{result[1]} Lvl: {result[2]}")
            else:
                cur.execute(f"SELECT * FROM GUILD_{ctx.guild.id} WHERE user_id={user.id}")
                result = cur.fetchone()
                if result!=None:
                    await ctx.channel.send(f"{user.mention} Exp:{result[1]} Lvl: {result[2]}")
                else:
                    await ctx.channel.send("How no such user in db")
        except sqlite3.OprationalError:
            await ctx.channel.send("Something went wrong when opening db")
            """
            
async def setup(bot):
    await bot.add_cog(Level(bot))