from django.contrib import admin
from .models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")
    search_fields = ("title", "author__username")
    list_filter = ("author", "author__username")

    admin.site.register(Publication,)
