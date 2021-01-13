from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from flashcard_app.models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def newCard(request):
    return render(request, 'newCard.html')

def addCard(request):
    if len(request.POST) < 1:
        return redirect('/new')
    errors= Card.objects.card_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    category= request.POST['category']
    question= request.POST['question']
    answer= request.POST['answer']
    category= str(category).lower()
    question= str(question).lower()
    answer= str(answer).lower()
    Card.objects.create(
        category= category,
        question= question,
        answer= answer
    )
    return redirect(categories)

def categories(request):
    cards= Card.objects.all()
    if len(cards) > 0:
        cardSet= set()
        for card in cards:
            cardSet.add(card.category)
        
        card_dict= {}
        for cat in cardSet:
            card_update= {cat : Card.objects.filter(category=cat).count()}
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

    cards= Card.objects.filter(category= category_id)
    context_cards = {}

    for card in cards:
        context_cards.update({card.id:card.question})
    print(context_cards)
    context= {
        "cards": context_cards,
        "deck_cat": category_id
    }
    # print(context)
    return render(request, 'card.html', context)

def login(request):
    return render(request, 'login.html')

def adLogin(request):
    hash= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    if bcrypt.checkpw('root'.encode(), hash.encode()):
        request.session['sesh']= hash
        return redirect(categories)
    else:
        return redirect(login)

def logout(request):
    if 'sesh' in request.session:
        del request.session['sesh']
        return redirect(login)
    else:
        return redirect(categories)

def delete(request, card_id):
    if 'sesh' not in request.session:
        return redirect(index)
    Card.objects.get(id=card_id).delete()
    return redirect(categories)

def getCategoryCards(request, category_id):
    cards= Card.objects.filter(category= category_id)
    deck= {}
    counter = 0;
    for card in cards:
        card_obj= {
                counter : {
                    "id" : card.id,
                    "question" : card.question,
                    "answer" : card.answer
                    }
        }
        deck.update(card_obj)
        counter+=1;
    
    return JsonResponse(deck)

#   for testing only
def test(request):
    print("*"*20)
    print("TEST")
    print("*"*20)
    return JsonResponse({"mtest" : "TEST"})