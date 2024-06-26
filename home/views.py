from django.shortcuts import render
from .models import Update

# Create your views here.
def index(request):
    """ A view to return the index page """
    update = Update.objects.all()

    context = {
        'update': update,
    }
    
    return render(request, 'home/index.html', context)


