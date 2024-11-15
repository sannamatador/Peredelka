from django.contrib import admin
from .models import Games


@admin.register(Games)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Register your models here.
