from django.contrib import admin
from .models import Url


# Register your models here.
class UrlAdmin(admin.ModelAdmin):
    list_display = ('link', 'uuid', 'created_at')
    list_filter = (['created_at'])


admin.site.register(Url, UrlAdmin)
