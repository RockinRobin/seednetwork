from django.db import models
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.
class Seed(models.Model):
     user = models.ForeignKey(User)
     seed_type = models.CharField(max_length=150, blank=True)
     crop_type = models.CharField(max_length=150, blank=True)
     grain_subcategory=models.CharField(max_length=50, blank=True)
     seed_variety = models.CharField(max_length=150, blank=True)
     seed_description = models.TextField(blank=True)
     enough_to_share = models.BooleanField(default=False)
     year = models.CharField(max_length=150, blank=True)
     origin = models.CharField(max_length=150, blank=True)

     archived = models.BooleanField(default=False, blank=False)

     more_info = models.BooleanField(default=False)

     def __unicode__(self):
         return self.user.username + "\'s " + self.seed_type 

     def __str__(self):
         return self.user.username + "\'s " + self.seed_type 

class ExtendedView(models.Model):
     parent_seed = models.ForeignKey(Seed)
     improvement_status = models.CharField(max_length=30, blank=True)
     growth_habit = models.CharField(max_length=30, blank=True)
     lodging = models.CharField(max_length=3, blank=True)
     cultivation = models.TextField(blank=True)
     disease = models.TextField(blank=True)
     days_to_maturity = models.IntegerField(null=True,blank=True)
     threshing = models.TextField(blank=True)
     cold_hardiness = models.TextField(blank=True)
     culinary_qualities = models.TextField(blank=True)
     other_uses = models.TextField(blank=True)
     additional_info = models.TextField(blank=True)
     external_url = models.URLField(blank=True) 

class Event(models.Model):
	name = models.CharField(max_length=150, blank=True)
	date = models.DateField()
	show_on_seed_edit = models.BooleanField(default=True)
	seed = models.ManyToManyField(Seed, blank=True)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

