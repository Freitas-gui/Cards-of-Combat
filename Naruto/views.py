from django.shortcuts import render
from .models import Card

def showCard(request):
    data = {}
    data['cards'] = Card.objects.all()
    return render(request, 'Naruto/allCards.html',data)