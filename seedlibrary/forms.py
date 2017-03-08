from django import forms
from seednetwork.forms import SeedNetworkBaseForm
from seedlibrary.models import Event

GRAIN_CHOICES = ( 
        ('-','-'),
        ('amaranth','Amaranth'),
        ('barley', 'Barley'),
#        ('buckwheat', 'Buckwheat'),
#        ('bulghur', 'Bulghur'),
        ('corn', 'Corn'),
        ('einkorn', 'Einkorn'),
        ('emmer', 'Emmer'),
#        ('fonio', 'Fonio'),
#        ('freekeh', 'Freekeh'),
#        ('kamut', 'Kamut'),
#        ('kaniwa', 'Kaniwa'),
        ('millet', 'Millet'),
        ('oats', 'Oats'),
#        ('quinoa', 'Quinoa'),
        ('rice', 'Rice'),
        ('rye', 'Rye'),
        ('sorghum', 'Sorghum'),
        ('spelt', 'Spelt'),
#        ('teff', 'Teff'),
#        ('triticale', 'Triticale'),
        ('wheat', 'Wheat'),
#        ('wild rice', 'Wild rice')
)

GRAIN_SUBCATEGORIES = (
	('-','-'),
	('common', 'Barley: Common'),
	('hulless','Barley: Hulless'),
	('dent', 'Corn: Dent'),
	('flint', 'Corn: Flint'),
	('flour', 'Corn: Flour'),
	('popcorn', 'Corn: Popcorn'),
	('sweet', 'Corn: Sweet'),
	('summer', 'Einkorn: Summer'),
	('winter', 'Einkorn: Winter'),
        ('summer', 'Emmer: Summer'),
        ('winter', 'Emmer: Winter'),
        ('common', 'Oats: Common'),
        ('hulless', 'Oats: Hulless'),
        ('dryland', 'Rice: Dryland'),
        ('paddy', 'Rice: Paddy'),
        ('perennial', 'Rye: Perennial'),
        ('summer', 'Rye: Summer'),
        ('winter', 'Rye: winter'),
        ('broom', 'Sorghum: Broom'),
        ('grain', 'Sorghum: Grain'),
        ('sweet', 'Sorghum: Sweet'),
        ('summer', 'Spelt: Summer'),
        ('winter', 'Spelt: Winter'),
        ('spring', 'Wheat: Spring'),
        ('winter', 'Wheat: Winter'),
        ('facultative', 'Wheat: Facultative'),
)
	




class GrainForm(SeedNetworkBaseForm):
	required_css_class = 'required'
#	seed_type = forms.CharField(label="Seed Type", max_length=150, required=False, help_text="i.e. grain, vegetable, herb, perennial, fruit bush, fruit tree, etc.")
	crop_type = forms.ChoiceField(label="Grain", choices=GRAIN_CHOICES, required=False)
	seed_variety = forms.CharField(label="Variety Name", max_length=150, required=True, help_text="e.g. Ukrainka, PI 356457 etc.")
	seed_description = forms.CharField(label="Grain Description", widget=forms.Textarea(attrs={'rows':'2', 'cols':'60'}), required=False, help_text="Briefly highlight defining characteristics. This text will appear in the Short Description column on the Browse Seeds page. Longer descriptions available in \"More Info\". ")
	enough_to_share = forms.BooleanField(label="Availability", required=False, help_text="Is seed available for sharing or purchase? Please indicate terms on member profile page.")
	year = forms.CharField(label="Year", max_length=150, required=False, help_text="What year was your seed grown?")
	origin = forms.CharField(label="Source", max_length=150, required=False, help_text="The year and from whom you first obtain the seed.")
#	events = forms.ModelMultipleChoiceField(Event.objects.filter(show_on_seed_edit=True), required=False, widget=forms.CheckboxSelectMultiple, help_text="What events will you bring the seed to?")
	more_info = forms.BooleanField(label="More Information", required=False, help_text="Do you want to provide more detailed information?")

class ExtendedGrainForm(SeedNetworkBaseForm):
	grain_subcategory=forms.ChoiceField(choices=GRAIN_SUBCATEGORIES,required=False)
	breed =forms.ChoiceField(label="Improvement Status", choices=(('-','-'),('landrace','Landrace'),('cultivar','Cultivar')),required=False)
	plant_timing=forms.ChoiceField(label="Growth Habit", choices=(('-','-'),('spring','Spring'),('winter','Winter'),('facultative','Facultative'), ('perennial','Perennial')),required=False)
        days_to_maturity=forms.IntegerField(label="Days to Maturity", required=False)
        lodging=forms.ChoiceField(choices=(('-','-'),('root','Root'),('stem','Stem'),('root&stem','Root & stem')), required=False)
	lodging_percent=forms.DecimalField(max_digits=4,decimal_places=2, required=False)
	disease=forms.CharField(label="Disease",widget=forms.Textarea(attrs={'rows':'3', 'cols':'60'}), required=False, help_text="What diseases, if any, affected this crop and to what extent did they affect the harvest?")
	threshing=forms.CharField(label="Processing",widget=forms.Textarea( attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Describe ease or difficulty of threshing, shelling, dehulling?")
	cold_hardiness=forms.CharField(label="Cold Hardiness", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Susceptibility to frost/freeze damage in spring/fall/winter?")
	culinary_qualities=forms.CharField(label="Culinary Qualities", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Breads, pastry, pasta, whole grain salads, low-gluten baking, beer...")
	other_traits=forms.CharField(label="Uses", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Culinary?, Livestock feed?, Straw for bedding?, Broom-making?, etc")
	external_url=forms.URLField(label="External URL", required=False)

class SeedExportForm(SeedNetworkBaseForm):
	archive = forms.BooleanField(required=False, help_text="Do you want to export your archived seed listings?")
