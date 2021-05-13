from django.contrib import admin

from.models import*

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
      
    list_display = ['id','name','country','population']

class ProfileAdmin(admin.ModelAdmin):

    list_display=['id','user','location','birth_date']

admin.site.register(Country)

admin.site.register(City,CountryAdmin)

admin.site.register(Profile,ProfileAdmin)

admin.site.register(Passengers)