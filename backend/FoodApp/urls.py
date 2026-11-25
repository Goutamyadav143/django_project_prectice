

from django.urls import path
from .views import *

urlpatterns = [
    path('menu',getAllmenuIteams),
    path('menu/<int:id>',getOneMenuIteam),
    path('menu/add',addItems)
   
]