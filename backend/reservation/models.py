from django.db import models
from users.models import CustomUser
from evenment.models import Evenement
# Create your models here.

class Reservation(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reservations')
    evenement= models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='reservations')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="date de reservation")

    def __str__(self):
        return f' Reservation du participant : {self.user.username} -- evenement : {self.evenement.name}'
