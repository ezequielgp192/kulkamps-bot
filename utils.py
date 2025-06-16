import requests

TELEGRAM_TOKEN = "7845477326:AAFiIEP8gL-yrpwBx49dKu_UYN1nznW3yu0"
TELEGRAM_CHAT_ID = 1192512385

def obter_jogos():
    # Simulação de jogos com ID
    return [
        {
            'id': 1,
            'liga': 'Premier League',
            'casa': 'Manchester City',
            'fora': 'Arsenal',
            'gols_casa': 2,
            'gols_fora': 1,
            'finalizacoes': 10,
        },
        {
            'id': 2,
            'liga': 'La Liga',
            'casa': 'Real Madrid',
            'fora': 'Barcelona',
            'gols_casa': 0,
            'gols_fora': 0,
            'finalizacoes': 7,
        }
    ]

def formatar_mensagem(jogo):
    return (
        f"⚽ {jogo['liga']}\n"
        f"{jogo['casa']} {jogo['gols_casa']} x {jogo['gols_fora']} {jogo['fora']}\n"
        f"Finalizações: {jogo['finalizacoes']}\n"
    )

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto
    }
    response = requests.post(url, data=payload)
    if not response.ok:
        print(f"[ERRO] Falha ao enviar mensagem: {response.text}")
