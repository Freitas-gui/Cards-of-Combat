from django.shortcuts import render, redirect
from .models import Card
from .Form import formCard

def allCards(request):
    data = {}
    data['cards'] = Card.objects.all()
    return render(request, 'Naruto/allCards.html',data)

def showCard(request , pk):
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