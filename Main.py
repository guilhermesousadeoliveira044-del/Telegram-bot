from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import time
import random
from datetime import datetime, timedelta, timezone

TOKEN = "8750926473:AAE3bxIVNiTeJP2ZyhwXakDNcF7aofIvIg0"
CHAT_ID = -1003900576949

bot = Bot(token=TOKEN)

mensagens = [
    "🐯 SINAL CONFIRMADO 🐯",
    "🔥 ENTRADA LIBERADA 🔥",
    "🚨 OPORTUNIDADE AGORA 🚨"
]

brasilia_tz = timezone(timedelta(hours=-3))

def gerar_sinal():
    modo = random.choice(["normal", "auto"])

    if modo == "normal":
        normal = random.randint(2, 7)
        turbo = random.randint(2, 7)
        rodadas_texto = f"🐯 Rodadas Normal: {normal}\n⚡ Rodadas Turbo: {turbo}"
    else:
        tipo_auto = random.choice(["turbo", "normal"])
        if tipo_auto == "turbo":
            rodadas_texto = "⚡ 10 Rodadas Automáticas (Turbo)"
        else:
            rodadas_texto = "🐯 10 Rodadas Automáticas (Normal)"

    jogo = random.choice(["Fortune Tiger 🐯", "Fortune Rabbit 🐰"])

    # 🔥 validade aleatória 2 a 5 minutos
    validade = random.randint(2, 5)

    aposta = random.choice(["R$0,40", "R$0,80"])
    msg_base = random.choice(mensagens)
    hora = datetime.now(brasilia_tz).strftime("%H:%M")

    legenda = f"""{msg_base}

🎮 Jogo: {jogo}

{rodadas_texto}

💰 Aposta sugerida: {aposta}

⏰ Validade: {validade} minutos
📍 Hora (Brasília): {hora}

⚠️ Use com responsabilidade
"""

    botoes = [
        [InlineKeyboardButton("🎮 JOGAR AGORA", url="https://57wina62.com/?pid=443235579")]
    ]

    reply_markup = InlineKeyboardMarkup(botoes)

    msg = bot.send_message(
        chat_id=CHAT_ID,
        text=legenda,
        reply_markup=reply_markup
    )

    return msg, validade


def rodar_bot():
    while True:
        msg, validade = gerar_sinal()

        # espera o tempo do sinal
        time.sleep(validade * 60)

        # edita pra expirado
        try:
            bot.edit_message_text(
                chat_id=CHAT_ID,
                message_id=msg.message_id,
                text="❌ SINAL EXPIRADO ❌\nAguarde o próximo sinal..."
            )
        except:
            pass

        # já manda outro direto (sem esperar)
        

rodar_bot()