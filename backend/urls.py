from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail<int:detail_id>/', detail, name='detail'),
    path("search/", search_detail, name="search_detail"),
    path("haftaliktavarlar/", haftaliktavarlar, name="haftaliktavarlar"),
    path("seller/", sotuvchi_bolish, name="sotuvchi_bolish"),
    path("saralangan/", saralangan, name="saralangan"),
    path("katalog/", katalog, name="katalog"),
    path("punkt/", punkt, name='punkt'),
    path('maxfiylik_kelishuvi/', maxfiylik_kelishuvi, name='maxfiylik_kelishuvi'),
    path('category/<str:category>/', narsalar_list, name='narsalar_list'),
    path('category/', narsalar_list, name='narsalar_all'),
    path('savat/' , savat, name='savat'),
    path('rasmiylashtirish/' , rasmiylashtirish, name='rasmiylashtirish'),  
    path('savol' , savol, name='savol'),

    # rasmilashtirish tepadagi  chekout 
]

