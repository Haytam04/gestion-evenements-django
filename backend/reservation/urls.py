from django.urls import path
from .views import reservationView
from base.views import HomeView
from evenment.views import EvenmentView


urlpatterns =[
    path('reserver/<int:id>',reservationView.as_view(),name='reservation'),
    path('evenment/',EvenmentView.as_view(),name='redirection')
]