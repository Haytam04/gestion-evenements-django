from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
import random
from datetime import datetime, timedelta
from evenment.models import Category, Evenement  # Make sure to use your correct app name

class Command(BaseCommand):
    help = 'Populates the database with fake categories and events'

    def handle(self, *args, **options):
        fake = Faker()
        
        # Create some categories first
        categories = ['Music', 'Sports', 'Business', 'Technology', 'Art', 'Food']
        for cat_name in categories:
            Category.objects.get_or_create(
                name=cat_name,
                slug=slugify(cat_name)
            )  # This closing parenthesis was missing
        
        # Get all categories
        all_categories = Category.objects.all()
        
        # Status choices from the model
        status_choices = ['draft', 'cancelled', 'onhold', 'confirmed']
        
        # Create 50 fake events
        for _ in range(50):
            # Random date between now and 1 year from now
            start_date = datetime.now() + timedelta(days=random.randint(1, 365))
            
            event = Evenement.objects.create(
                name=fake.sentence(nb_words=4),
                description=fake.text(max_nb_chars=500),
                date=start_date,
                lieu=fake.city(),
                nombre_places=random.randint(10, 500),
                statue=random.choice(status_choices),
                category=random.choice(all_categories) if all_categories else None
            )
            
            self.stdout.write(f'Created event: {event.name}')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with events'))