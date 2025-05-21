from django.shortcuts import render,get_object_or_404,redirect

from django.views import View
from evenment.models import Evenement
from users.models import CustomUser
from .models import Reservation
from django.views.generic import ListView
from django.contrib import messages
from django.utils import timezone


class reservationView(View):
        def post(self, request, id):
            try:
                # Get the event or return 404
                evenement = get_object_or_404(Evenement, id=id)
                
                
                # Check if user is authenticated
                if request.user.is_authenticated:
                    reservation, created = Reservation.objects.get_or_create(
                        evenement=evenement,  
                        user=request.user,
                        created_at=timezone.now(),
                    )
                else:
                    # Handle anonymous user
                    if not request.session.session_key:
                        request.session.create()
                    
                    # Create or get reservation for anonymous user
                    reservation, created = Reservation.objects.get_or_create(
                        evenement=evenement,  # Changed from event to evenement
                        session_key=request.session.session_key,
                        user=None,
                        created_at=timezone.now(),
                    )
                
                if created:
                    messages.success(request, "Reservation created successfully!")
                    # Decrement available places
                    evenement.nombre_places += 1
                    evenement.save()
                else:
                    messages.info(request, "You already have a reservation for this event")
                
                return redirect('redirection')
                
            except Exception as e:
                messages.error(request, f"Error creating reservation: {str(e)}")
                return redirect('redirection')