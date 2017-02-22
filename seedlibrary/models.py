from django.db import models
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.
class Seed(models.Model):
     user = models.ForeignKey(User)
     seed_type = models.CharField(max_length=150, blank=True)
     crop_type = models.CharField(max_length=150, blank=True)
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
     grain_subcategory=models.CharField(max_length=50, blank=True)
     breed = models.CharField(max_length=30, blank=True)
     plant_timing = models.CharField(max_length=30, blank=True)
     lodging = models.CharField(max_length=30, blank=True)
     lodging_percent = models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
     disease = models.CharField(max_length=150, blank=True)
     days_to_maturity = models.IntegerField(null=True,blank=True)
     threshing = models.CharField(max_length=150, blank=True)
     cold_hardiness = models.CharField(max_length=150, blank=True)
     culinary_qualities = models.CharField(max_length=150, blank=True)
     other_traits = models.CharField(max_length=150, blank=True)
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

