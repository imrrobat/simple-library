from django.shortcuts import HttpResponse, redirect
from .models import Book
from author.models import Author

def home(request):
    all_books = Book.objects.all()

    l = [f'{b.title} written by {b.author.name}' for b in all_books]
    content = '<br>'.join(l)

    return HttpResponse(f'<center><h1>Book List:<hr>{content}</h1></center>')

def add_book(request, id, title):
    selected_author = Author.objects.get(id=id)
    Book.objects.create(title=title, author = selected_author)

    return redirect('home')

# remove book 

# update book 
