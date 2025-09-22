import discord
from discord.ext import commands
import random

# Stelle hier deinen Bot-Token ein
TOKEN = "DEIN_DISCORD_BOT_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ist jetzt online – Willkommen bei der Bundesagentur für Arbeit!")

# Command: !wartezeit
@bot.command()
async def wartezeit(ctx):
    wochen = random.randint(2, 12)
    embed = discord.Embed(
        title="Bundesagentur für Arbeit",
        description=f"Ihre geschätzte Wartezeit beträgt **{wochen} Wochen**.",
        color=discord.Color.red()
    )
    embed.set_footer(text="Dies ist ein automatisch erstelltes Schreiben. Bitte antworten Sie nicht.")
    await ctx.send(embed=embed)

# Command: !leistung
@bot.command()
async def leistung(ctx):
    embed = discord.Embed(
        title="Leistungsbescheid",
        description="Sie erhalten Arbeitslosengeld in Höhe von **0,00 €**.",
        color=discord.Color.red()
    )
    embed.set_footer(text="Bitte reichen Sie einen neuen Antrag ein.")
    await ctx.send(embed=embed)

# Command: !maßnahme
@bot.command(name="maßnahme")
async def massnahme(ctx):
    massnahmen = [
        "Bewerbungstraining: Wie öffne ich Word 2003",
        "Maßnahme: Pünktliches Erscheinen üben",
        "Fortbildung: Stuhlkreis für Fortgeschrittene",
        "Schulung: Einführung in das Faxgerät"
    ]
    auswahl = random.choice(massnahmen)
    embed = discord.Embed(
        title="Zuweisung zu einer Maßnahme",
        description=f"Sie wurden eingeteilt für: **{auswahl}**",
        color=discord.Color.red()
    )
    embed.set_footer(text="Ihre Anwesenheit ist verpflichtend.")
    await ctx.send(embed=embed)

# Command: !termin
@bot.command()
async def termin(ctx):
    embed = discord.Embed(
        title="Terminvereinbarung",
        description="Ihr nächster Termin ist am **14. März 2026 um 07:15 Uhr**.",
        color=discord.Color.red()
    )
    embed.set_footer(text="Sollten Sie diesen Termin verpassen, droht eine Leistungskürzung.")
    await ctx.send(embed=embed)

bot.run(TOKEN)
