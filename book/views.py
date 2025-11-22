from django.shortcuts import HttpResponse, redirect
from .models import Book
from author.models import Author

def home(request):
    all_books = Book.objects.all()

    l = [f'{b.id}.{b.title} written by {b.author.name} <a href="/remove/{b.id}">delete</a><br>' for b in all_books]
    content = '<br>'.join(l)

    return HttpResponse(f'<center><h1>Book List:<hr>{content}</h1></center>')

def add_book(request, id, title):
    selected_author = Author.objects.get(id=id)
    Book.objects.create(title=title, author = selected_author)

    return redirect('home')

# remove book 
def remove_book(request, id):
    sel_book = Book.objects.get(id=id)
    sel_book.delete()
    return redirect('home')

# update book 
def update_book(request, id, new_name):
    selected_book = Book.objects.get(id=id)
    selected_book.title = new_name 
    selected_book.save()
    
    # Book.objects.filter(id=id).update(name=new_name)

    return redirect('home')
    