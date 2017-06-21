from django.contrib import admin
from seedlibrary.models import Seed, ExtendedView, Event

class SeedAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 
                     'crop_type', 'grain_subcategory', 'seed_variety', 'enough_to_share')
    search_fields = ['crop_type', 'grain_subcategory', 'seed_variety']
    list_filter = ['crop_type','grain_subcategory', 'enough_to_share']
   
    def name(self, instance):
       return instance.user.first_name + ' ' + instance.user.last_name
    def email(self, instance):
       return instance.user.email

class ExtendedViewAdmin(admin.ModelAdmin):
    list_display = ('variety', 'subcategory', 'type', 'parent_seed')
    search_fields = ['other_uses', 'additional_info']

    def variety(self,instance):
       return instance.parent_seed.seed_variety
    def subcategory(self,instance):
       return instance.parent_seed.grain_subcategory
    def type(self,instance):
       return instance.parent_seed.crop_type
    
admin.site.register(Seed,SeedAdmin)
admin.site.register(ExtendedView, ExtendedViewAdmin)
#admin.site.register(Event)
