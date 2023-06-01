from django.contrib import admin

# Register your models here.
from service.models import offerOrder

class rqOffer(admin.ModelAdmin):
    list_display=('need', 'package', 'name', 'mail', 'sms')
admin.site.register(offerOrder, rqOffer) 