from django.contrib import admin
from seedlibrary.models import Seed, Event

class SeedAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 
                     'crop_type', 'grain_subcategory', 'seed_variety', 'enough_to_share')
    search_fields = ['crop_type', 'grain_subcategory', 'seed_variety']
    list_filter = ['crop_type','grain_subcategory', 'enough_to_share']
   
    def name(self, instance):
       return instance.user.first_name + ' ' + instance.user.last_name
    def email(self, instance):
       return instance.user.email
    
admin.site.register(Seed,SeedAdmin)
#admin.site.register(Event)
