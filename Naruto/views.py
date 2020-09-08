from django.shortcuts import render, redirect
from .models import Card
from .Form import formCard
from django.contrib.auth.decorators import login_required

# For do search of Cards
from django.db.models import Q
from django.views.generic import ListView

@login_required
def allCards(request):
    '''
        Show all cards existing in database.
        :return render: A template that content list of cards and options
            of interaction, like the (search and new card).

    '''
    data = {}
    data['cards'] = Card.objects.all()
    return render(request, 'Naruto/allCards.html',data)

@login_required
def oneCard(request , pk):
    '''
        Show one card with pk value.
        :return render: A template that content the card selected and options
            of interaction, like the (update and delete).
    '''
    data = {}
    data['card'] = Card.objects.get(pk=pk)
    return render(request, 'Naruto/oneCard.html',data)

@login_required
def createCard(request):
    ''' Form used for create a new card. '''
    data = {}
    form = formCard(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_allCards')
    data['form'] = form
    return render(request , 'Naruto/form_new_card.html' , data)

@login_required
def update(request , pk):
    ''' Form used for update a card with pk value. '''
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
    ''' Exclude a card of the database with pk value. '''
    card = Card.objects.get(pk=pk)
    card.delete()
    return redirect('url_allCards')


class SearchResultsView(ListView):
    '''
        Search per cards with start of name and exact level specified by the user.
        :param ListView: A page representing a list of objects.
    '''
    model = Card
    template_name = 'Naruto/cards_search_list.html'

    def get_queryset(self): # new
        '''
            Catch the name or/and level specified per user;
            Do a filter in database;
            Keep a list of cards of search.
            :return object_list : list of cards of search.
        '''
        # Name specified per user;
        query_name = self.request.GET.get('q_name')
        # Level specified per user;
        query_level = self.request.GET.get('q_level')
        # Case no specific the level
        if query_level == '':
            object_list = Card.objects.filter(
                Q(name__startswith=query_name)
                )
        # All others cases
        else:
            object_list = Card.objects.filter(
                Q(name__startswith=query_name) & Q(level__exact=query_level)
            )
        return object_list