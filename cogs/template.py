from io import BytesIO
import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import FFmpegPCMAudio
from discord.ui import Select, View
from helpers import checks
from PIL import Image, ImageChops, ImageDraw, ImageFont

# Menu selection class
def circle(pfp, size= (215, 215)):
    
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot


    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.hybrid_command(
        name="play",
        description="Play a music on voice",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    async def play(self,ctx):
        
        if (ctx.author.voice):
          channel = ctx.message.author.voice.channel
          voice = await channel.connect()
          await ctx.send("I joined")
          source = FFmpegPCMAudio('song.mp3')
          voice.play(source)
          await ctx.send("Playing Centimeter 「Hatsune Miku Cover」 (Koruru remix)")
          
        else:
          await ctx.send("You not join channel voice pls join channel voice")
    
    @commands.hybrid_command(
        name="leave",
        description="Leave bot from voice"
      
      )
    
    async def leave(self, ctx):
      if (ctx.guild.voice_client):
        await ctx.voice_client.disconnect()
        await ctx.send("I leave")
      else:
        await ctx.send("I'm not in a voice channel")
        
        
    @commands.hybrid_command(
        name="profile",
        description="Display your profile info"
      
      )
    async def profile(self,ctx,member:discord.Member=None):
      if not member:
          member = ctx.author
          
      
      name, nick, Id, status = str(member), member.display_name, str(member.id), str(member.status).upper()
      created_at = member.created_at.strftime("%a %b\n%B %Y")
      joined_at = member.joined_at.strftime("%a %b\n%B %Y")
      money,level = "99999","1000"
      azuxi = "Azuxi Unix"
      
      base = Image.open("base.png").convert("RGBA")
      background = Image.open("bg.png").convert("RGBA")
      userAvatar = member.display_avatar
      pfp = userAvatar
      data = BytesIO(await pfp.read())
      pfp = Image.open(data).convert("RGBA")
      
      name = f"{name[:16]}.." if len(name)>16 else name
      nick = f"AZXI - {nick[:17]}.." if len(nick)>17 else f"AZXI - {nick}"
      
      draw = ImageDraw.Draw(base)
      pfp = circle(pfp,(215,215))
      font = ImageFont.truetype("name_font.ttf",38)
      akafont = ImageFont.truetype("font.ttf",30)
      subfont = ImageFont.truetype("font.ttf",25)
      copy = ImageFont.truetype("font.ttf",20)
      
      
      draw.text((280,240),name,font = font)
      draw.text((270,315),nick,font = akafont)
      draw.text((65,490),Id,font = subfont)
      draw.text((405,490),status,font = subfont)
      draw.text((65,635),money,font = subfont)
      draw.text((405,635),level,font = subfont)
      draw.text((65,770),created_at,font = subfont)
      draw.text((405,770),joined_at,font = subfont)
      draw.text((300,860),azuxi,fill=(255,255,255,90),font = copy)
      base.paste(pfp,(56,158),pfp)
      
      background.paste(base,(0,0),base)
      
      with BytesIO() as a:
          background.save(a,"PNG")
          a.seek(0)
          await ctx.send(file = discord.File(a, "profile.png"))
      
# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Template(bot))
