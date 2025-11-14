from .views import home, add_book
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('add/<int:id>/<title>/', add_book, name='add_book')
]
