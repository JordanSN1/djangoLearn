import requests

anime_url = "https://api.jikan.moe/v4/anime"
manga_url = "https://api.jikan.moe/v4/manga"

def get_anime_list(limit=20, page=1):
    params = {
        'limit': limit,  # Nombre d'éléments par page
        'page': page      # Numéro de page
    }
    
    response = requests.get(anime_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        anime_list = []
        
        if 'data' in data:
            for anime in data['data']:
                title = anime['title']
                description = anime.get('synopsis', 'Description non disponible')
                image_url = anime['images']['jpg'].get('image_url', 'Image non disponible')
                
                # Vérification de la clé 'popularityRank' dans les données de l'API
                popularity_rank = anime.get('popularityRank', 'Non spécifié')

                anime_info = {
                    'title': title,
                    'description': description,
                    'image_url': image_url,
                    'popularityRank': popularity_rank
                }
                anime_list.append(anime_info)
        
        pagination_info = data.get('pagination', {})
        return anime_list, pagination_info
    else:
        return {"error": f"Erreur HTTP {response.status_code}"}

def get_manga_list(limit=20, page=1):
    params = {
        'limit': limit,  # Nombre d'éléments par page
        'page': page      # Numéro de page
    }
    
    response = requests.get(manga_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        manga_list = []
        
        if 'data' in data:
            for manga in data['data']:
                title = manga['title']
                description = manga.get('synopsis', 'Description non disponible')
                image_url = manga['images']['jpg'].get('image_url', 'Image non disponible')

                manga_info = {
                    'title': title,
                    'description': description,
                    'image_url': image_url,
                }
                manga_list.append(manga_info)

        pagination_info = data.get('pagination', {})
        return manga_list, pagination_info
    else:
        return {"error": f"Erreur HTTP {response.status_code}"}
