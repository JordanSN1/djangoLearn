from django.shortcuts import render
from .api2 import get_anime_list, get_manga_list

def anime_manga_list_view(request):
    # Paramètres de pagination
    page = int(request.GET.get('page', 1))  # Page actuelle
    limit = 20  # Limite d'éléments par page
    
    # Récupérer les données des animes et mangas
    anime_list, anime_pagination = get_anime_list(limit=limit, page=page)
    manga_list, manga_pagination = get_manga_list(limit=limit, page=page)
    
    # Variables de pagination
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if 'has_next_page' in anime_pagination and anime_pagination['has_next_page'] else None
    
    return render(
        request,
        'anime2.html',
        {
            'anime_list': anime_list,
            'manga_list': manga_list,
            'prev_page': prev_page,
            'next_page': next_page,
            'current_page': page,
        }
    )
