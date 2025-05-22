from django.urls import path
from .views import EvenmentView,EvenmentDetailView,categorieView,categorieDetailView,EvenmentCreation,creationView,editpageView,delete_item
from reservation.views import reservationView
urlpatterns =[
    path('',EvenmentView.as_view(),name='evenment'),
    path('Evenment/<int:pk>',EvenmentDetailView.as_view(),name='evenment_detail'),
    path('ctegorie',categorieView.as_view(),name='categorie_list'),
    path('ctegorie/<int:pk>',categorieDetailView.as_view(),name='categoriel'),
    path('edit/<int:pk>',editpageView.as_view(),name='edit'),
    path('cree',EvenmentCreation.as_view(),name='cree'),
    path('creation',creationView.as_view(),name='creation'),
    
    
    
    
    
    path('deleate/<int:pk>',delete_item,name='supprimer'),

    

    
]