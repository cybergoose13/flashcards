from django.shortcuts import render, redirect
from flashcard_app.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def newCard(request):
    return render(request, 'newCard.html')

def addCard(request):
    card= Card.objects.create(
        catagory= request.POST['catagory'],
        question= request.POST['question'],
        answer= request.POST['answer'],
        wrong_one= request.POST['wrong_one'],
        wrong_two= request.POST['wrong_two'],
        wrong_three= request.POST['wrong_three'],
        created_by= request.POST['creator']
    )
    return redirect(catagories)

def catagories(request):
    cards= Card.objects.all()
    if len(cards) > 0:
        cardSet= set()
        for card in cards:
            cardSet.add(card.catagory)
        
        card_dict= {}
        for cat in cardSet:
            card_update= {cat : Card.objects.filter(catagory=cat).count()}
            # card_dict[cat]= Card.objects.filter(catagory=cat).count()
            card_dict.update(card_update)
            print(cat)
        context= {
            'cards': cards,
            'catagories': cardSet,
            'card_dict': card_dict
        }
        return render(request, 'catagories.html', context)
    return render(request, 'catagories.html')

#   for testing only
def test(request):
    return render(request, 'test.html')