import requests

# URL de base de l'API pour animes et mangas
anime_url = "https://kitsu.io/api/edge/anime"
manga_url = "https://kitsu.io/api/edge/manga"

def get_anime_list(limit=40):
    # Limiter le nombre de résultats à `limit`
    params = {'page[limit]': limit}  # Limite le nombre d'animes récupérés
    response = requests.get(anime_url, params=params)
    
    # Vérifier si la réponse de l'API est valide
    if response.status_code == 200:
        try:
            data = response.json()  # Parse la réponse JSON
        except ValueError:
            return {"error": "Erreur lors du parsing de la réponse JSON"}
        
        # Vérifier si 'data' existe dans la réponse
        if 'data' not in data:
            return {"error": "Données manquantes dans la réponse"}
        
        anime_list = []
        
        # Parcourir les données des animes
        for anime in data['data']:
            # Utiliser get() pour éviter des erreurs si certaines clés sont manquantes
            title = anime['attributes'].get('canonicalTitle', 'Titre non disponible')
            description = anime['attributes'].get('description', 'Description non disponible')
            
            # Gérer l'absence de l'image
            image_url = anime['attributes'].get('posterImage', {}).get('original', 'Image non disponible')
            
            # Ajouter les informations dans la liste
            anime_info = {
                'title': title,
                'description': description,
                'image_url': image_url  # Récupère l'image si disponible
            }
            anime_list.append(anime_info)
            print(response.text)  # Affiche la réponse brute de l'API pour déboguer

        
        return anime_list
    else:
        return {"error": f"Erreur HTTP {response.status_code}"}
    

def get_manga_list(limit=20):
    # Limiter le nombre de résultats à `limit`
    params = {'page[limit]': limit}  # Limite le nombre de mangas récupérés
    response = requests.get(manga_url, params=params)
    
    if response.status_code == 200:
        data = response.json()  # Parse la réponse JSON
        manga_list = []
        
        # Vérification que la clé 'data' existe dans la réponse
        if 'data' in data:
            for manga in data['data']:
                # Vérifier que les informations nécessaires existent avant de les utiliser
                title = manga['attributes'].get('canonicalTitle', 'Titre non disponible')
                description = manga['attributes'].get('description', 'Description non disponible')
                image_url = manga['attributes']['posterImage'].get('original', 'Image non disponible')
                
                manga_info = {
                    'title': title,
                    'description': description,
                    'image_url': image_url  # Récupère l'image
                }
                manga_list.append(manga_info)
        else:
            return {"error": "Aucune donnée disponible"}
        
        return manga_list
    else:
        return {"error": response.status_code}

# Exemple d'utilisation des fonctions pour récupérer les listes d'animes et de mangas
animes = get_anime_list(limit=40)
mangas = get_manga_list(limit=20)