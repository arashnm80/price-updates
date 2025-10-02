import requests
import json
from datetime import datetime

# URL de l'API
API_URL = "https://sarfe.erfjab.com/api/prices"

# Chemin vers ton fichier JSON
PRICES_FILE = "prices.json"

def fetch_prices():
    response = requests.get(API_URL, headers={"accept": "application/json"})
    response.raise_for_status()  # pour lever une exception en cas d'erreur
    return response.json()

def save_prices(data):
    # Extraire les données nécessaires
    usd_price = data.get("usd1")
    eur_price = data.get("eur1")
    last_modified = data.get("last_modified")

    # Structure selon ton format
    result = {
        "last_modified": last_modified,
        "USD": usd_price,
        "EUR": eur_price
    }

    # Écriture dans le fichier
    with open(PRICES_FILE, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    try:
        data = fetch_prices()
        save_prices(data)
        print("✅ Fichier prices.json mis à jour.")
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour : {e}")
