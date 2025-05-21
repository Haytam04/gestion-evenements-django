from django.urls import path
from .views import EvenmentView,EvenmentDetailView,categorieView,categorieDetailView,EvenmentCreation
from reservation.views import reservationView
urlpatterns =[
    path('',EvenmentView.as_view(),name='evenment'),
    path('Evenment/<int:pk>',EvenmentDetailView.as_view(),name='evenment_detail'),
    path('ctegorie',categorieView.as_view(),name='categorie_list'),
    path('ctegorie/<int:pk>',categorieDetailView.as_view(),name='categoriel'),
    path('cree',EvenmentCreation.as_view(),name='cree'),
    

    
]