from django.http import HttpResponse
from django.http import Http404
from .models import Book
from django.template import loader
from django.shortcuts import  render, get_object_or_404
# Create your views here.



def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'all_books': all_books,
    }
    return render(request,'books/index.html',context)

def detail(request,book_id):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except Book.DoesNotExist:
    #     raise Http404("Book Does not exist")
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'books/detail.html', context)