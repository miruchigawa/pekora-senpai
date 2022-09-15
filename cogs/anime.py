import animec
from animec import Anilyrics
import discord
from discord.ext import commands

class Anime(commands.Cog, name="Anime"):
  
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(
        name="anime",
        description="Getting anime info and other stuff"
      
      )
    async def anime(self,ctx,*,query):
      try:
        
        anime = animec.Anime(query)
      except:
        
        await ctx.send(embed= discord.Embed(description= "⚠️No corresponding anime in query", color= discord.Color.red()))
        
        return
    
      embed = discord.Embed(title = anime.title_english,url = anime.url,description= f"{anime.description[:200]}...",color = discord.Color.random())
      embed.add_field(name= "Episodes", value= str(anime.episodes))
      embed.add_field(name= "Rating", value= str(anime.rating))
      embed.add_field(name= "Broadcast", value= str(anime.broadcast))
      embed.add_field(name= "Status", value= str(anime.status))
      embed.add_field(name= "Type", value= str(anime.type))
      embed.add_field(name= "Is Nsfw", value= str(anime.is_nsfw()))
      embed.set_thumbnail(url= anime.poster)
      await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Anime(bot))