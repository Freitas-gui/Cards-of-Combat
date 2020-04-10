from django.shortcuts import render, redirect
from .models import Card
from .Form import formCard

def allCards(request):
    data = {}
    data['cards'] = Card.objects.all()
    return render(request, 'Naruto/allCards.html',data)

def oneCard(request , pk):
    data = {}
    data['card'] = Card.objects.get(pk=pk)
    return render(request, 'Naruto/oneCard.html',data)

def createCard(request):
    data = {}
    form = formCard(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_allCards')
    
    data['form'] = form
    return render(request , 'Naruto/form.html' , data)

def update(request , pk):
    data = {}
    card = Card.objects.get(pk=pk)
    form = formCard(request.POST or None , instance=card)

    if form.is_valid():
        form.save()
        return redirect('url_allCards')
    
    data['form'] = form
    data['card'] = card
    return render(request , 'Naruto/form.html' , data)

def delete(request , pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return redirect('url_allCards')
