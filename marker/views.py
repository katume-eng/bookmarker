from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Impression


# Create your views here.

def index(request):
    return render(request, 'marker/index.html')

def booklist(request):
    return render(request, 'marker/booklist.html',{'books':Book.objects.all()})

def record(request):
    return render(request, 'marker/record.html')

def book_detail(request, book_id):
    try:
        book = Book.ebjects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
    impressions = Impression.objects.filter(book=book)
    context = {
        'book': book,
        'impressions': impressions
    }
    return render(request, 'marker/book_detail.html', context)