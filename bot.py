import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def stock(ctx):
    try:
        with open("stock.txt", "r") as file:
            data = file.readlines()

        if not data:
            await ctx.send("📭 Stock kosong!")
            return

        embed = discord.Embed(
            title="🌱 STOCK TANAMAN GAG 2",
            color=discord.Color.green()
        )

        for line in data:
            if "=" in line:
                nama, stok = line.strip().split("=")
                embed.add_field(
                    name=nama.strip(),
                    value=f"Stock: {stok.strip()}",
                    inline=False
                )

        embed.set_footer(text="Live Stock • GAG 2 Stock ID")
        await ctx.send(embed=embed)

    except FileNotFoundError:
        await ctx.send("❌ File stock.txt belum ada!")

@bot.command()
async def addstock(ctx, *, item: str):
    with open("stock.txt", "a") as file:
        file.write(f"{item}\n")
    await ctx.send(f"✅ **{item}** ditambah ke stock!")

@bot.command()
async def clearstock(ctx):
    open("stock.txt", "w").close()
    await ctx.send("🗑️ Stock udah dihapus!")

bot.run(TOKEN)