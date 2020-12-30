from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def newDeck(request):
    return render(request, 'newDeck.html')

def availableDeck(request):
    return render(request, 'availableDeck.html')

#   for testing only
def test(request):
    return render(request, 'test.html')