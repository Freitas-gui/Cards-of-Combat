from django.shortcuts import render, redirect
from .models import Card
from .Form import formCard
from django.contrib.auth.decorators import login_required


@login_required
def allCards(request):
    data = {}
    data['cards'] = Card.objects.all()
    return render(request, 'Naruto/allCards.html',data)

@login_required
def oneCard(request , pk):
    data = {}
    data['card'] = Card.objects.get(pk=pk)
    return render(request, 'Naruto/oneCard.html',data)

@login_required
def createCard(request):
    data = {}
    form = formCard(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_allCards')
    
    data['form'] = form
    return render(request , 'Naruto/form_new_card.html' , data)

@login_required
def update(request , pk):
    data = {}
    card = Card.objects.get(pk=pk)
    form = formCard(request.POST or None, request.FILES or None , instance=card)

    if form.is_valid():
        form.save()
        return redirect('url_allCards')
    
    data['form'] = form
    return render(request , 'Naruto/form_update_card.html' , data)

@login_required
def delete(request , pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return redirect('url_allCards')