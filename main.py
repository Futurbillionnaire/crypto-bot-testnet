import time
import random
from datetime import datetime

# Capital initial
capital = 1000.0
profit_total = 0.0
reinvest_percent = 0.5
interval_seconds = 10  # Délai entre chaque cycle en secondes

# Liste des cryptos simulées
cryptos = [
    "SOL", "XRP", "TRX", "MATIC", "AVAX", "ADA",
    "DOT", "ATOM", "LINK", "LTC", "NEAR", "APT",
    "ARB", "OP", "ETC", "XLM", "FIL", "EOS",
    "BCH", "FTM"
]

def simulate_arbitrage(crypto):
    logs = []
    for mode in ["spot", "crosschain"]:
        if random.random() < 0.5:
            spread = random.uniform(0.5, 3.0)  # % de gain
            gain = round(capital * (spread / 100) * reinvest_percent, 4)
            logs.append((f"🔁 Arbitrage {mode} {crypto}", gain))
    return logs

def simulate_sniping():
    if random.random() < 0.2:
        gain = round(random.uniform(1.0, 3.0) * reinvest_percent, 4)
        return ("🎯 Snipe token", gain)
    return None

def simulate_flash_loans():
    if random.random() < 0.1:
        gain = round(random.uniform(5.0, 10.0) * reinvest_percent, 4)
        return ("⚡ Flash loan", gain)
    return None

def simulate_airdrop():
    if random.random() < 0.3:
        gain = round(random.uniform(0.5, 2.0) * reinvest_percent, 4)
        return ("🎁 Airdrop", gain)
    return None

def simulate_yield():
    gain = round(capital * random.uniform(0.0005, 0.0015) * reinvest_percent, 4)
    return ("🌾 Yield farming", gain)

def simulate_node_reward():
    if random.random() < 0.5:
        gain = round(random.uniform(0.3, 1.2) * reinvest_percent, 4)
        return ("🟢 Node reward", gain)
    return None

def simulate_trading():
    gain = round(random.uniform(0.5, 1.5) * reinvest_percent, 4)
    return ("📈 Trading automatique", gain)

def simulate_cycle():
    global capital, profit_total
    logs = []

    # Arbitrage sur toutes les cryptos
    for crypto in cryptos:
        logs.extend(simulate_arbitrage(crypto))

    # Autres modules
    for fn in [
        simulate_sniping,
        simulate_flash_loans,
        simulate_airdrop,
        simulate_yield,
        simulate_node_reward,
        simulate_trading
    ]:
        result = fn()
        if result:
            logs.append(result)

    gain_total = sum(gain for _, gain in logs)
    capital += gain_total
    profit_total += gain_total

    # Affichage
    print("\n📊 NOUVELLE BOUCLE")
    print(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Capital : €{capital:,.2f}")
    for label, gain in logs:
        print(f"{label} → +€{gain}")
    print(f"\n💰 Profit cette boucle : +€{gain_total:.2f}")
    print(f"💼 Total cumulé : €{capital:,.2f}")
    print("=" * 60)

if __name__ == "__main__":
    while True:
        simulate_cycle()
        time.sleep(interval_seconds)
