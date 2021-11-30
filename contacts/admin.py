from django.contrib import admin
from .models import contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','car_title','city','create_date')
    list_display_links = ('id','first_name')
    search_fields = ('first_name', 'last_name', 'email','car_title')
    list_per_page = 25

admin.site.register(contact, contactAdmin)