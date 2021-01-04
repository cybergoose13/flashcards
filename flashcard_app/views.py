from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from flashcard_app.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def newCard(request):
    return render(request, 'newCard.html')

def addCard(request):
    category= request.POST['catagory']
    question= request.POST['question']
    answer= request.POST['answer']
    wrong1= request.POST['wrong_one']
    wrong2= request.POST['wrong_two']
    wrong3= request.POST['wrong_three']
    creator= request.POST['creator']
    category= str(category).lower()
    question= str(question).lower()
    answer= str(answer).lower()
    wrong1= str(wrong1).lower()
    wrong2= str(wrong2).lower()
    wrong3= str(wrong3).lower()
    creator= str(creator).lower()
    Card.objects.create(
        catagory= category,
        question= question,
        answer= answer,
        wrong_one= wrong1,
        wrong_two= wrong2,
        wrong_three= wrong3,
        created_by= creator
    )
    return redirect(categories)

def categories(request):
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
            'categories': cardSet,
            'card_dict': card_dict
        }
        return render(request, 'categories.html', context)
    return render(request, 'categories.html')


def card(request, category_id):

    cards= Card.objects.filter(catagory= category_id)
    context_cards = {}

    for card in cards:
        context_cards.update({card.id:card.question})
    print(context_cards)
    context= {
        "cards": context_cards
    }
    print(context)
    return render(request, 'card.html', context)

#   for testing only
def test(request):
    print("*"*20)
    print("TEST has been called. . . .")
    data={
        "mTest": "TEST"
    }
    return JsonResponse(data)