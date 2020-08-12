from django.shortcuts import render, redirect
from .models import Card
from .Form import formCard
from django.contrib.auth.decorators import login_required

# For do search of Cards
from django.db.models import Q
from django.views.generic import ListView

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


class SearchResultsView(ListView):
    model = Card
    template_name = 'Naruto/cards_search_list.html'

    def get_queryset(self): # new
        query_name = self.request.GET.get('q_name')
        query_level = self.request.GET.get('q_level')
        if query_level == '':
            object_list = Card.objects.filter(
                Q(name__startswith=query_name)
                )
        else:
            object_list = Card.objects.filter(
                Q(name__startswith=query_name) & Q(level__exact=query_level)
            )
        return object_list