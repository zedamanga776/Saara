from cordscript import Client 
import warnings
import sqlite3
import asyncio
import discord
import os
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

db = sqlite3.connect("banco.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    F INTEGER DEFAULT 0
)
""")

db.commit()

bot = Client(
    token=os.getenv("DISCORD_TOKEN"),
    prefix="s",
    insensitive=True)

# Informações

bot.command(
name="ping",
code=" $addTextDisplay[Atualmente conto com **$ping** de ping para rodar meus **comandos**!] $addSeparator[true;small] $addTextDisplay[## 🏓 | Pong!]"
)

bot.command(
name="info",
code="$thumbnail[$userAvatar]"
"$title[📖 | Informações!]"
"$description[> Olá $username, Bem vindo ao meu centro de informações, Utilize o painel abaixo para verificar minhas informações e tudo oque tenho a oferecer, Divirta-se comigo!]"
"$color[#ADD8E6]"
"$footer[👾 | Utilizado por $username]"
"$addButton[Owner;ow;primary] $addButton[Info;inf;secondary] $addButton[Ideia;id;success]"
)

bot.command(
name="avatar",
code="$title[🖼  | Lindo avatar de <@$mentioned[1;yes]>] $description[$image[$userAvatar[$mentioned[1;yes]]]] $footer[Comando utilizado por $username] $color[#ADD8E6]"
)


# Owners

bot.command(
name="ev",
code="$if[$authorID!=1188581439395074059;"
"Acesso Negado!, Este comando e restrito para Adiministradore, Utilize outros comandos!;$eval[$message]]"
)

bot.command(
name="help",
aliases=["ajuda", "comandos", "commands"],
code="$addContainer[$addTextDisplay[## ℹ️ | Informações]" 
"$addTextDisplay[Avatar - Veja a foto de perfil da pessoa marcada]"
"$adxTextDisplay[Info - Veja as informações do bot]"
"$addTextDisplay[Ping - Veja a latencia do bot]"
"$addSeparator[true;small]"
"$addTextDisplay[## 💸 | Economia]"
"$addTextDisplay[Em breve...];#ADD8E6]"
)


# Eventos

@bot.event
async def on_ready():
    print("✅️ | Bot Iniciado Com Sucesso!")
    asyncio.create_task(status_loop())

async def status_loop():
    status_messages = [
        ("🖥 | Estou em {} servidores", discord.ActivityType.playing),
        ("💬 | Com {} usuários", discord.ActivityType.watching),
        ("🎮 | Saara em {} servidores", discord.ActivityType.playing),
    ]
    
    index = 0
    while True:
        try:
            message, activity_type = status_messages[index]
            activity = discord.Activity(
                type=activity_type,
                name=message.format(len(bot.guilds))
            )
            await bot.change_presence(activity=activity)
            index = (index + 1) % len(status_messages)
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Erro ao mudar status: {e}")
            await asyncio.sleep(5)

# Interações

bot.interaction(customId="inf", 
code=
"$addSection[$username;thumbnail;$userAvatar]"
"$defer $addContainer[C;$addTextDisplay[# ℹ️ | Informações]"
"$addSeparator[true;small]"
"$addTextDisplay[> Olá $username, Eu sou saara, criado em 17 de junho, Fui feita pra ser sua companheira Ferminina no discord, Tenho 18 anos e estou pronta pra te acompanhar!];#ADD8E6]"
)

bot.run()