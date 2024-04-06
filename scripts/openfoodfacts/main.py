import requests

# URL de l'API Open Food Facts
api_url = "https://world.openfoodfacts.org/api/v0/product/{}.json"

# Récupération des informations sur le produit en utilisant son code barre
product_code = "7622210449313"
response = requests.get(api_url.format(product_code))

# Vérification de la réponse
if response.status_code == 200:
    product_data = response.json()

    # Affichage des informations nutritionnelles
    print("Informations nutritionnelles pour le produit : {}".format(product_data["product"]["product_name"]))
    print("Calories : {}".format(product_data["product"]["nutriments"].get("energy-kcal_100g", "Inconnu")))
    print("Lipides : {}".format(product_data["product"]["nutriments"].get("fat_100g", "Inconnu")))
    print("Sodium : {}".format(product_data["product"]["nutriments"].get("sodium_100g", "Inconnu")))
    print("Glucides : {}".format(product_data["product"]["nutriments"].get("carbohydrates_100g", "Inconnu")))
    print("Fibres alimentaires : {}".format(product_data["product"]["nutriments"].get("fiber_100g", "Inconnu")))
    print("Sucres : {}".format(product_data["product"]["nutriments"].get("sugars_100g", "Inconnu")))
    print("Protéines : {}".format(product_data["product"]["nutriments"].get("proteins_100g", "Inconnu")))
else:
    print("Une erreur est survenue lors de la récupération des données")
