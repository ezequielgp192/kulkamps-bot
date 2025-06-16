import time
from utils import obter_jogos, formatar_mensagem, enviar_mensagem

print("[START] Bot iniciado...")

enviados = set()

while True:
    try:
        jogos = obter_jogos()

        for jogo in jogos:
            jogo_id = jogo.get("id")
            if jogo_id is None or jogo_id in enviados:
                continue

            mensagem = formatar_mensagem(jogo)
            enviar_mensagem(mensagem)
            print(f"[INFO] Enviada: {mensagem.strip()}")
            enviados.add(jogo_id)

    except Exception as e:
        print("[ERRO] Erro na execução:", e)

    time.sleep(60)
