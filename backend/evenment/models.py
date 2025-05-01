from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models

class Evenement(models.Model):
    STATUE_CHOICES = (
        ('draft', 'Draft'),               
        ('published', 'Published'),       
        ('cancelled', 'Cancelled'),       
        ('postponed', 'Postponed'),       
        ('completed', 'Completed'),       
        ('archived', 'Archived'), 
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    nombre_places = models.IntegerField()
    image = models.ImageField(null=True, upload_to='products/')
    statue = models.CharField(
        max_length=100,
        choices=STATUE_CHOICES,
        default='draft'  
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='evenements'
    )


    def __str__(self):
        return self.name
