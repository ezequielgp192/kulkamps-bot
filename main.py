
import time
from utils import obter_jogos_ao_vivo, extrair_estatisticas, formatar_mensagem
from telegram import enviar_telegram

def run_bot():
    print("[START] Bot iniciado e monitorando jogos em tempo real...")
    while True:
        try:
            jogos = obter_jogos_ao_vivo()
            print(f"[INFO] {len(jogos)} jogos encontrados ao vivo.")
            for jogo in jogos:
                try:
                    nome = f"{jogo['homeTeam']['name']} vs {jogo['awayTeam']['name']}"
                    chutes, escanteios, ataques, posse, tempo, finalizacoes = extrair_estatisticas(jogo)
                    print(f"[CHECK] Verificando: {nome}")
                    if tempo >= 15 and chutes >= 5 and finalizacoes >= 10:
                        mensagem = formatar_mensagem(jogo)
                        if mensagem:
                            enviar_telegram(mensagem)
                            print("[SINAL] Enviado!")
                        else:
                            print("[ERRO] Mensagem nula.")
                    else:
                        print(f"[SKIP] Sem sinal: {nome}")
                except Exception as e:
                    print(f"[ERRO] Falha no jogo: {e}")
            print("[WAIT] Aguardando 5 minutos...")
            time.sleep(300)
        except Exception as e:
            print(f"[ERRO] Erro geral: {e}")
            time.sleep(60)

if __name__ == "__main__":
    run_bot()
