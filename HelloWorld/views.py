from django.shortcuts import render

def page_view(request):
    return render(request,'temp.html')
    