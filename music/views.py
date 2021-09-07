from django.shortcuts import render
from .models import Book
# Create your views here.
def index_view(request):

    return render(request,'music/temp1.html')



def allbook(request):
    books = Book.objects.filter(id__contains='1')
    return render(request,'music/all_book.html',locals())
    
