"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views

urlpatterns = [
    path('api/collector_edition',views.fetch_or_create_ce,name='Fetch Collector Edition by name'),
    path('api/collector_edition/author',views.fetch_ce_author,name='Fetch Collector Edition by Author name'),
    path('api/collector_edition/game',views.fetch_ce_game_name,name='Fetch Collector Edition by Game name'),
    path('api/collector_edition/random',views.fetch_ce_random,name='Fetch n Random Collector Editions'),
    path('api/collector_edition/price',views.fetch_ce_price,name='Fetch Collector Editions based on Price'),
]