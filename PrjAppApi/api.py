import requests

anime_url = "https://kitsu.io/api/edge/anime"
manga_url = "https://kitsu.io/api/edge/manga"
import requests

anime_url = "https://kitsu.io/api/edge/anime"

def get_anime_list(limit=20, offset=0):
    params = {
        'page[limit]': limit, 
        'page[offset]': offset,
        'sort': '-popularityRank'  # Trie par popularité décroissante
    }

    response = requests.get(anime_url, params=params)

    # Vérifier si la réponse est correcte
    if response.status_code == 200:
        data = response.json()
        
        # Vérifier que 'data' existe dans la réponse
        if 'data' in data:
            anime_list = []

            for anime in data['data']:
                # Vérifier que 'attributes' et 'posterImage' existent dans chaque anime
                if 'attributes' in anime and 'posterImage' in anime['attributes']:
                    title = anime['attributes'].get('canonicalTitle', 'Titre non disponible')
                    description = anime['attributes'].get('description', 'Description non disponible')
                    image_url = anime['attributes']['posterImage'].get('original', 'Image non disponible')
                    popularity_rank = anime['attributes'].get('popularityRank', 'Non disponible')

                    # Ajouter à la liste des animes
                    anime_info = {
                        'title': title,
                        'description': description,
                        'image_url': image_url,
                        'popularity_rank': popularity_rank
                    }
                    anime_list.append(anime_info)
            
            # Retourner la liste des animes
            return anime_list

        else:
            return {"error": "Aucune donnée disponible"}
    
    else:
        return {"error": f"Erreur HTTP {response.status_code}"}

def get_manga_list(limit=20, offset=0):
    # Paramètre de tri par popularité décroissante et limitation des résultats
    params = {
        'page[limit]': limit, 
        'page[offset]': offset,
        'sort': '-popularityRank'  # Trie par popularité (du plus populaire au moins populaire)
    }
    
    response = requests.get(manga_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            manga_list = []
            for manga in data['data']:
                title = manga['attributes'].get('canonicalTitle', 'Titre non disponible')
                description = manga['attributes'].get('description', 'Description non disponible')
                image_url = manga['attributes']['posterImage'].get('original', 'Image non disponible')
                
                # Vérifier la présence du champ 'popularityRank' et l'ajouter à la liste
                popularity_rank = manga['attributes'].get('popularityRank', None)
                
                if popularity_rank is not None:
                    manga_info = {
                        'title': title,
                        'description': description,
                        'image_url': image_url,
                        'popularity_rank': popularity_rank  # Inclure le rang de popularité pour le tri
                    }
                    manga_list.append(manga_info)
                else:
                    # Gérer les cas où il manque un rang de popularité
                    print(f"Rang de popularité manquant pour le manga {title}")
            
            # Tri explicite de la liste par 'popularity_rank' en ordre décroissant
            manga_list.sort(key=lambda x: x['popularity_rank'], reverse=True)
            return manga_list
        
        else:
            print("Erreur dans les données retournées par l'API")
            return {"error": "Aucune donnée disponible"}
    
    else:
        return {"error": f"Erreur HTTP {response.status_code}"}
