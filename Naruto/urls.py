from Naruto.views import oneCard, allCards, createCard, update, delete, SearchResultsView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('allCards/',allCards,name = 'url_allCards'),
    path('createCard/',createCard,name = 'url_createCard'),
    path('oneCard/<int:pk>/',oneCard,name = 'url_oneCard'),
    path('update/<int:pk>',update,name = 'url_update'),
    path('delete/<int:pk>',delete,name = 'url_delete'),
    path('search/',SearchResultsView.as_view(), name = 'url_search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


