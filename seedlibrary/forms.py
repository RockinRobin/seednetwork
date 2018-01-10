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
        ('grain', 'Amaranth: Grain'),
        ('leaf', 'Amaranth: Leaf'),
	('common', 'Barley: Common'),
	('hulless','Barley: Hulless'),
	('dent', 'Corn: Dent'),
	('flint', 'Corn: Flint'),
	('flour', 'Corn: Flour'),
	('popcorn', 'Corn: Popcorn'),
	('sweet', 'Corn: Sweet'),
	('spring', 'Einkorn: Spring'),
	('winter', 'Einkorn: Winter'),
        ('spring', 'Emmer: Spring'),
        ('winter', 'Emmer: Winter'),
        ('common', 'Oats: Common'),
        ('hulless', 'Oats: Hulless'),
        ('dryland', 'Rice: Dryland'),
        ('paddy', 'Rice: Paddy'),
        ('perennial', 'Rye: Perennial'),
        ('spring', 'Rye: Spring'),
        ('winter', 'Rye: Winter'),
        ('broom', 'Sorghum: Broom'),
        ('grain', 'Sorghum: Grain'),
        ('sweet', 'Sorghum: Sweet'),
        ('spring', 'Spelt: Spring'),
        ('winter', 'Spelt: Winter'),
        ('spring', 'Wheat: Spring'),
        ('winter', 'Wheat: Winter'),
        ('facultative', 'Wheat: Facultative'),
)
	




class GrainForm(SeedNetworkBaseForm):
	required_css_class = 'required'
#	seed_type = forms.CharField(label="Seed Type", max_length=150, required=False, help_text="i.e. grain, vegetable, herb, perennial, fruit bush, fruit tree, etc.")
	crop_type = forms.ChoiceField(label="Grain", choices=GRAIN_CHOICES, required=True)
	grain_subcategory=forms.ChoiceField(label="Grain Subcategory", choices=GRAIN_SUBCATEGORIES,required=True)
	seed_variety = forms.CharField(label="Variety Name", max_length=150, required=True, help_text="e.g. Ukrainka, PI 356457 etc.")
	seed_description = forms.CharField(label="Short Description", widget=forms.Textarea(attrs={'rows':'2', 'cols':'60'}), required=False, help_text="Briefly highlight defining characteristics. This text will appear in the Short Description column on the Browse Seeds page. Longer descriptions available in \'More Information\'. ")
	enough_to_share = forms.BooleanField(label="Availability", required=False, help_text="Is your seed available for sharing or purchase? Please indicate terms on member profile page.")
	year = forms.CharField(label="Year", max_length=150, required=False, help_text="What year was your seed grown?")
	origin = forms.CharField(label="Source", max_length=150, required=False, help_text="The year and from whom you first obtained the seed.")
#	events = forms.ModelMultipleChoiceField(Event.objects.filter(show_on_seed_edit=True), required=False, widget=forms.CheckboxSelectMultiple, help_text="What events will you bring the seed to?")
	more_info = forms.BooleanField(label="More Information", required=False, help_text="Check the box to provide more detailed information that will be available on the seed's profile page.")

class ExtendedGrainForm(SeedNetworkBaseForm):
	improvement_status =forms.ChoiceField(label="Improvement Status", choices=(('-','-'),('landrace','Landrace'),('cultivar','Cultivar'),('unknown','Unknown')),required=False)
	growth_habit=forms.ChoiceField(label="Growth Habit", choices=(('-','-'),('spring','Spring'),('winter','Winter'),('facultative','Facultative'), ('perennial','Perennial')),required=False)
        days_to_maturity=forms.IntegerField(label="Days to Maturity", required=False, help_text="Enter only a single number, even if that is an estimate.")
        lodging=forms.ChoiceField(choices=(('-','-'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9')), required=False, help_text="1 = no lodging, 9 = all plants flat.")
	cultivation=forms.CharField(label="Cultivation",widget=forms.Textarea( attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Bed preparation, spacing, interplanting, fertility needs, pest protection, grown organically?")
	cold_hardiness=forms.CharField(label="Cold Hardiness", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Susceptibility to frost/freeze damage in spring/fall/winter? For example, \'A freak mid-June frost did not seem to slow down growth at all in USDA zone 5a.\'")
	disease=forms.CharField(label="Disease",widget=forms.Textarea(attrs={'rows':'3', 'cols':'60'}), required=False, help_text="Describe disease resistance or susceptibility of variety.")
	threshing=forms.CharField(label="Threshing",widget=forms.Textarea( attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Describe ease or difficulty of threshing, shelling, dehulling.")
	cold_hardiness=forms.CharField(label="Cold Hardiness", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Susceptibility to frost/freeze damage in spring/fall/winter? For example, \'A freak mid-June frost did not seem to slow down growth at all in USDA zone 5a.\'")
	culinary_qualities=forms.CharField(label="Culinary Qualities", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Baking, cooking, or brewing qualities and uses.")
	other_uses=forms.CharField(label="Other Uses", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Livestock feed, bedding, broom-making, straw weaving, thatching,  etc.")
	additional_info=forms.CharField(label="Additional Information", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Interesting history, cultural information, etc.")
	external_url=forms.URLField(label="External URL", required=False, help_text="Include a link to a website with related information, or to your own website.")

class SeedExportForm(SeedNetworkBaseForm):
	archive = forms.BooleanField(required=False, help_text="Do you want to export your archived seed listings?")
