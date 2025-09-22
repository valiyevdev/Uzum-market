from django.urls import path
from .views import *

urlpatterns = [
   path("dashboard/",  dashboard, name="dashboard"),
   path('mahsulotlar/', mahsulotlar, name='mahsulotlar'),
   path('buyurtmalar/', buyurtmalar, name='buyurtmalar'),
   path('mijozlar/', mijozlar, name='mijozlar'),
   path('hisobotlar/', hisobotlar, name='hisobotlar'),
   path('adminnav/', adminnav, name='adminnav'),
   path('adminbars/', adminbars, name='adminbars'),
]