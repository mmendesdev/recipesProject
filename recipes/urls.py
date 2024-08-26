from django.contrib import path
from recipes.views import contato, home, sobre

urlpatterns = [ 
    path("home", home),
    path('sobre/', sobre),
    path('contato', contato),
]
