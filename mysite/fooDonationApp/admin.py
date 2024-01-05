from django.contrib import admin
from .models import Donate, ReceiverUser

# Register your models here.
class DonateAdmin(admin.ModelAdmin):
    list_display= ['id',"donarName","donarEmail","category"]
    search_fields= ['id']

class ReceiverUserAdmin(admin.ModelAdmin):
    list_display= ['id',"receiver_meal","receiver_name","receiver_email"]
    search_fields= ['id']

admin.site.register(Donate, DonateAdmin)
admin.site.register(ReceiverUser, ReceiverUserAdmin)
