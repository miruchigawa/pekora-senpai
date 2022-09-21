import animec
import discord
from aiohttp import ClientSession
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
    
    async def GetNsfw(self, tag):
      async with ClientSession() as r:
        async with r.get(f"https://api.waifu.im/random/?selected_tags={tag}") as i:
          data = await i.json()
      return data['images'][0]['url']
    
    @commands.hybrid_command(
        name="nsfw",
        description="Show nsfw commands"
      )
    
    async def nsfw(self, ctx,*, query):
      await ctx.send(
          embed=discord.Embed().set_image(url=await self.GetNsfw(f"{query}"))
        )
    
    @commands.hybrid_command(
        name="quoteanime",
        description="Get random anime quote"
      )
    
    async def quoteanime(self, ctx):
      session = await ClientSession().get('https://animechan.vercel.app/api/random')
      data = session.json()
      anime = data['anime']
      character = data['character']
      quote = data['quote']
      embed = discord.Embed(title = anime,description= character,color = discord.Color.random())
      embed.add_field(name= "Quote", value= quote)
      await ctx.send(embed=embed)
          

async def setup(bot):
    await bot.add_cog(Anime(bot))