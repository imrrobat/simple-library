from django.shortcuts import HttpResponse, redirect
from .models import Author

# alaki

def author_home(request):
    all_authors = Author.objects.all()

    l = [f'{aut.id}.{aut.name}' for aut in all_authors]
    content = '<br>'.join(l)

    return HttpResponse(f'<center><h1>Author List:<hr>{content}</h1></center>')

def add_author(request, name):
    Author.objects.create(name=name)
    return redirect('author_home')

def remove_author(reuqest, id):
    selected_author = Author.objects.get(id=id)
    selected_author.delete()
    return redirect('author_home')

# update author

# all books from a author