from django.shortcuts import render, redirect
from flashcard_app.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def newCard(request):
    return render(request, 'newCard.html')

def addCard(request):
    catagory= request.POST['catagory']
    question= request.POST['question']
    answer= request.POST['answer']
    wrong1= request.POST['wrong_one']
    wrong2= request.POST['wrong_two']
    wrong3= request.POST['wrong_three']
    creator= request.POST['creator']
    card= Card.objects.create(
        catagory= str(catagory).lower,
        question= str(question).lower,
        answer= str(answer).lower,
        wrong_one= str(wrong1).lower,
        wrong_two= str(wrong2).lower,
        wrong_three= str(wrong3).lower,
        created_by= str(creator).lower
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


def card(request):
    return render(request, 'card.html')

#   for testing only
def test(request):
    return render(request, 'test.html')