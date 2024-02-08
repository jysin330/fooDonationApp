from django.contrib import admin
from .models import DonateRecipe, ReceiverRecipe

# Register your models here.
class DonateAdmin(admin.ModelAdmin):
    list_display= ['id',"foodItem","slug","category"]
    search_fields= ['id']

class ReceiverUserAdmin(admin.ModelAdmin):
    list_display= ['id',"receiver_meal", "timestamp","update"]
    search_fields= ['id']

admin.site.register(DonateRecipe, DonateAdmin)
admin.site.register(ReceiverRecipe, ReceiverUserAdmin)
