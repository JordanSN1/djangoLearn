from django.urls import path
from . import views

# URLS configuration

urlpatterns = [

    # URL for the anime and manga list view
    path('anime_manga_list/', views.anime_manga_list_view, name='anime_manga_list'),
        


]