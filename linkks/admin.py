from django.contrib import admin
from linkks.models import Link
# Register your models here.



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'description', 'created_at', 'updated_at')
    search_fields = ('url', 'user__username')  # Permite buscar por el nombre de usuario
