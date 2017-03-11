from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from localflavor.us.models import PhoneNumberField, USPostalCodeField, USStateField, USZipCodeField

USDA_ZONE_CHOICES = ( 
        ('-', '-'),
        ('1a', '1a'),
        ('1b', '1b'),
        ('2a', '2a'),
        ('2b', '2b'),
        ('3a', '3a'),
        ('3b', '3b'),
        ('4a', '4a'),
        ('4b', '4b'),
        ('5a', '5a'),
        ('5b', '5b'),
        ('6a', '6a'),
        ('6b', '6b'),
        ('7a', '7a'),
        ('7b', '7b'),
        ('8a', '8a'),
        ('8b', '8b'),
        ('9a', '9a'),
        ('9b', '9b'),
        ('10a', '10a'),
        ('10b', '10b'),
        ('11a', '11a'),
        ('11b', '11b'),
        ('12a', '12a'),
        ('12b', '12b')
)


class MemberInfo(models.Model):
	user = models.ForeignKey(User)
	email_is_public = models.BooleanField(default=True)

	phone = PhoneNumberField(blank=True)
	phone_is_public = models.BooleanField(default=True)

	street_address = models.TextField(blank=True)
	street_address_is_public = models.BooleanField(default=True)

	mailing_address = models.TextField(blank=True)
	mailing_address_is_public = models.BooleanField(default=True)

	usda_zone = models.CharField(max_length=3, default='-', choices=USDA_ZONE_CHOICES)

	about_me = models.TextField(blank=True)
        external_url = models.URLField(blank=True)
	include_in_member_profiles = models.BooleanField(default=True)

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name
       
        @property
	def clean_street_address(self):
		return self.street_address.replace( '~', ',')
