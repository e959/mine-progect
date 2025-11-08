import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive

# تشغيل السيرفر الصغير للحفاظ على البوت Online
keep_alive()

# قراءة التوكن من متغير البيئة
TOKEN = os.getenv(""DISCORD_TOKEN")

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# حدث عند تشغيل البوت
@bot.event
async def on_ready():
    print(f"{bot.user} جاهز للعمل!")

# مثال أمر بسيط
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# تشغيل البوت
bot.run(TOKEN)
