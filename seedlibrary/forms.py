from django import forms
from seednetwork.forms import SeedNetworkBaseForm
from seedlibrary.models import Event

GRAIN_CHOICES = ( 
        ('-','-'),
        ('amaranth','Amaranth'),
        ('barley', 'Barley'),
        ('buckwheat', 'Buckwheat'),
        ('bulghur', 'Bulghur'),
        ('corn', 'Corn'),
        ('einkorn', 'Einkorn'),
        ('farro', 'Farro'),
        ('fonio', 'Fonio'),
        ('freekeh', 'Freekeh'),
        ('kamut', 'Kamut'),
        ('kaniwa', 'Kaniwa'),
        ('millet', 'Millet'),
        ('oats', 'Oats'),
        ('quinoa', 'Quinoa'),
        ('rice', 'Rice'),
        ('rye', 'Rye'),
        ('sorghum', 'Sorghum'),
        ('spelt', 'Spelt'),
        ('teff', 'Teff'),
        ('triticale', 'Triticale'),
        ('wheat', 'Wheat'),
        ('wild_rice', 'Wild Rice')
)


class GrainForm(SeedNetworkBaseForm):
#	seed_type = forms.CharField(label="Seed Type", max_length=150, required=False, help_text="i.e. grain, vegetable, herb, perennial, fruit bush, fruit tree, etc.")
	crop_type = forms.ChoiceField(label="Grain", choices=GRAIN_CHOICES, required=False)
	seed_variety = forms.CharField(label="Grain Variety", max_length=150, required=False, help_text="i.e. Ukrainka, PI 356457 etc.")
	seed_description = forms.CharField(label="Grain Description", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Landrace or cultivar?, When planted (S/F/Fac)?, Lodging?, Disease? Days to maturity? Threshing? Baking/Cooking Qualities? Cold Hardiness? Other traits? etc.")
	enough_to_share = forms.BooleanField(label="Available", required=False, help_text="Is seed available for purchase/free?")
	year = forms.CharField(label="Year", max_length=150, required=False, help_text="When did you grow out this seed?")
	origin = forms.CharField(label="Source", max_length=150, required=False, help_text="When and from whom  did you first obtain the seed?")
#	events = forms.ModelMultipleChoiceField(Event.objects.filter(show_on_seed_edit=True), required=False, widget=forms.CheckboxSelectMultiple, help_text="What events will you bring the seed to?")

class SeedExportForm(SeedNetworkBaseForm):
	archive = forms.BooleanField(required=False, help_text="Do you want to export your archived seed listings?")
