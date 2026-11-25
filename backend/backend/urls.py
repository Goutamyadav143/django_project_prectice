

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('food/',include("FoodApp.urls")),
    path('admin/', admin.site.urls),
]
