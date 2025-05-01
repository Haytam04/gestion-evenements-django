from django.contrib import admin
from .models import Evenement, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'lieu', 'statue', 'category')
    list_filter = ('date', 'category', 'statue')
    search_fields = ('name', 'description', 'lieu')

