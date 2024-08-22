from django.contrib import admin
from .models import Collaborateur

@admin.register(Collaborateur)
class CollaborateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')
