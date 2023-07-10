import requests
from bs4 import BeautifulSoup

# URL du site à scraper
base_url = "http://www.radiohead.fr/"

# Fonction pour récupérer le contenu d'une URL donnée
def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

# Fonction pour extraire les informations souhaitées d'une page
def parse_page_content(content):
    # Utilisez BeautifulSoup pour extraire les données nécessaires
    soup = BeautifulSoup(content, 'html.parser')
    
    # Parcourez et extrayez les informations selon vos besoins
    # Exemple : récupérez tous les liens de la page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

# Récupérez le contenu de la page d'accueil
homepage_content = get_page_content(base_url)

if homepage_content:
    # Analysez le contenu de la page d'accueil
    parse_page_content(homepage_content)

    # Trouvez tous les liens internes et visitez-les pour extraire davantage d'informations
    internal_links = BeautifulSoup(homepage_content, 'html.parser').find_all('a', href=True)
    for link in internal_links:
        # Construisez l'URL complète pour chaque lien interne
        url = base_url + link['href']
        # Récupérez le contenu de chaque lien interne
        page_content = get_page_content(url)
        if page_content:
            # Analysez le contenu de chaque lien interne
            parse_page_content(page_content)
        else:
            print(f"Impossible de récupérer le contenu de l'URL : {url}")
else:
    print("Impossible de récupérer le contenu de la page d'accueil.")
