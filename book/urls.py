from .views import home, add_book, remove_book, update_book
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('add/<int:id>/<title>/', add_book, name='add_book'),
    path('remove/<int:id>/', remove_book, name='remove_book'),
    path('edit/<int:id>/<new_name>/', update_book, name='update_book')
]
