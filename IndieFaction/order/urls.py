from django.urls import path

from . import views

urlpatterns = [
    path('api/print_order/', views.printOrder),
    path('api/completed_order/', views.completedOrder)
]
