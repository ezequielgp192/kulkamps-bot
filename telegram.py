
import requests

TOKEN = "7845477326:AAFiIEP8gL-yrpwBx49dKu_UYN1nznW3yu0"
CHAT_ID = "1192512385"  # Altere para o ID do grupo se necessário

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    try:
        r = requests.post(url, data=payload)
        if r.status_code == 200:
            print("[OK] Mensagem enviada com sucesso.")
        else:
            print(f"[ERRO] Falha ao enviar mensagem: {r.status_code}")
    except Exception as e:
        print(f"[ERRO] Telegram: {e}")
