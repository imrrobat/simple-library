from .views import author_home,add_author, remove_author
from django.urls import path

urlpatterns = [
    path('', author_home, name='author_home'),
    path('add/<name>/', add_author, name='add_author'),
    path('remove/<int:id>/', remove_author, name='remove_author')
]
