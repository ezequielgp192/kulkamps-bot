
from playwright.sync_api import sync_playwright
import json
import requests

def obter_jogos_ao_vivo():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.sofascore.com/football/livescore", timeout=60000)
            page.wait_for_selector("script#__NEXT_DATA__", state="attached")
            raw_json = page.locator("script#__NEXT_DATA__").inner_text()
            dados = json.loads(raw_json)
            eventos = dados.get("props", {}).get("pageProps", {}).get("initialState", {}).get("events", {}).get("events", [])
            return eventos
    except Exception as e:
        print(f"[ERRO] Falha ao acessar jogos ao vivo: {e}")
        return []

def obter_detalhes_jogo(event_id):
    try:
        estatisticas = requests.get(f"https://api.sofascore.com/api/v1/event/{event_id}/statistics").json()
        detalhes = requests.get(f"https://api.sofascore.com/api/v1/event/{event_id}").json()
        return detalhes, estatisticas
    except Exception as e:
        print(f"[ERRO] Detalhes jogo {event_id}: {e}")
        return {}, {}

def extrair_estatisticas(jogo):
    try:
        detalhes, estatisticas = obter_detalhes_jogo(jogo["id"])
        chutes = escanteios = ataques = posse_home = posse_away = finalizacoes = 0
        for grupo in estatisticas.get("statistics", []):
            for item in grupo.get("statisticsItems", []):
                nome = item["name"].lower()
                if "chutes a gol" in nome:
                    chutes += int(item["home"]) + int(item["away"])
                if "escanteios" in nome:
                    escanteios += int(item["home"]) + int(item["away"])
                if "ataques perigosos" in nome:
                    ataques += int(item["home"]) + int(item["away"])
                if "posse" in nome:
                    posse_home = int(item["home"].replace('%', ''))
                    posse_away = int(item["away"].replace('%', ''))
                if "finalizações" in nome or "chutes" in nome:
                    try:
                        finalizacoes += int(item["home"]) + int(item["away"])
                    except:
                        continue
        tempo = detalhes.get("event", {}).get("time", {}).get("minute", 0)
        posse = max(posse_home, posse_away)
        return chutes, escanteios, ataques, posse, tempo, finalizacoes
    except Exception as e:
        print(f"[ERRO] extração stats: {e}")
        return 0, 0, 0, 0, 0, 0

def formatar_mensagem(jogo):
    try:
        home = jogo['homeTeam']['name']
        away = jogo['awayTeam']['name']
        liga = jogo['tournament']['name']
        pais = jogo['tournament']['category']['name']
        id = jogo['id']
        slug = jogo.get('slug', "")
        link_sofa = f"https://www.sofascore.com/{slug}/{id}"
        link_bet365 = f"https://www.bet365.com/#/AX/K{home.replace(' ', '%20')}%20x%20{away.replace(' ', '%20')}"
        link_betano = f"https://www.betano.com/br/search/?query={home}%20x%20{away}"
        return (f"📡 SINAL AO VIVO - {liga} ({pais})\n"
                f"⚽ {home} x {away}\n"
                f"📺 SofaScore: {link_sofa}\n"
                f"🔗 Bet365: {link_bet365}\n"
                f"🔗 Betano: {link_betano}")
    except:
        return None
