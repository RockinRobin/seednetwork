from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from localflavor.us.models import PhoneNumberField, USPostalCodeField, USStateField, USZipCodeField

# Create your models here.

class MemberInfo(models.Model):
	user = models.ForeignKey(User)
	email_is_public = models.BooleanField(default=True)

	phone = PhoneNumberField(blank=True)
	phone_is_public = models.BooleanField(default=True)

	street_address = models.TextField(blank=True)
	street_address_is_public = models.BooleanField(default=True)

	mailing_address = models.TextField(blank=True)
	mailing_address_is_public = models.BooleanField(default=True)

	about_me = models.TextField(blank=True)
	include_in_member_profiles = models.BooleanField(default=True)

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name
       
        @property
	def clean_street_address(self):
		return self.street_address.replace( '~', ',')
