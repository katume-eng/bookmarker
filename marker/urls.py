from django.urls import path
from .views import index, booklist, record, book_detail

urlpatterns = [
    path('', index, name='index'),
    path('booklist/', booklist, name='booklist'),
    path('record/', record, name='record'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
]