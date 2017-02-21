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
        ('wild rice', 'Wild rice')
)

GRAIN_SUBCATEGORIES = (
	('-','-'),
	('a1','Amaranth: a1'),
	('a2','Amaranth: a2'),
	('whole', 'Barley: whole'),
	('hulled','Barley: hulled'),
	('hulless', 'Barley: hull-less'),
	('bw1', 'Buckwheat: bw1'),
	('bw2', 'Buckwheat: bw2'),
	('b1', 'Bulghur: b1'),
	('b2', 'Bulghur: b2'),
	('c1', 'Corn: c1'),
	('c2', 'Corn: c2'),
	('e1', 'Einkorn: e1'),
	('e2', 'Einkorn: e2'),
        ('fa1', 'Farro: fa1'),
        ('fa2', 'Farro: fa2'),
        ('fo1', 'Fonio: fo1'),
        ('fo2', 'Fonio: fo2'),
        ('fr1', 'Freekeh: fr1'),
        ('fr2', 'Freekeh: fr2'),
        ('km1', 'Kamut: km1t'),
        ('km2', 'Kamut: km2'),
        ('kn1', 'Kaniwa: kn1'),
        ('kn2', 'Kaniwa: kn2'),
        ('m1', 'Millet: m1'),
        ('m2', 'Millet: m2'),
        ('o1', 'Oats: o1'),
        ('o2', 'Oats: o2'),
        ('q1', 'Quinoa: q1'),
        ('q2', 'Quinoa: q2'),
        ('ri1', 'Rice: ri1'),
        ('ri2', 'Rice: ri2'),
        ('ry1', 'Rye: ry1'),
        ('ry2', 'Rye: ry2'),
        ('so1', 'Sorghum: so1'),
        ('so2', 'Sorghum: so2'),
        ('sp1', 'Spelt: sp1'),
        ('sp2', 'Spelt: sp2'),
        ('te1', 'Teff: t1'),
        ('te2', 'Teff: t2'),
        ('tr1', 'Triticale: tr1'),
        ('tr2', 'Triticale: tr2'),
        ('wh1', 'Wheat: wh1'),
        ('wh2', 'Wheat: wh2'),
        ('wi1', 'Wild rice: wi1'),
        ('wi2', 'Wild rice: wi2')
)
	




class GrainForm(SeedNetworkBaseForm):
#	seed_type = forms.CharField(label="Seed Type", max_length=150, required=False, help_text="i.e. grain, vegetable, herb, perennial, fruit bush, fruit tree, etc.")
	crop_type = forms.ChoiceField(label="Grain", choices=GRAIN_CHOICES, required=False)
	seed_variety = forms.CharField(label="Grain Variety", max_length=150, required=False, help_text="e.g.. Ukrainka, PI 356457 etc.")
	seed_description = forms.CharField(label="Grain Description", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Short headline (<75 chars) Longer descriptions available in \"More Info\". ")
	enough_to_share = forms.BooleanField(label="Available", required=False, help_text="Is seed available for purchase/free? Please indicate terms on member profile page.")
	year = forms.CharField(label="Year", max_length=150, required=False, help_text="What year was your seed grown?")
	origin = forms.CharField(label="Source", max_length=150, required=False, help_text="The year and from whom you first obtain the seed.")
#	events = forms.ModelMultipleChoiceField(Event.objects.filter(show_on_seed_edit=True), required=False, widget=forms.CheckboxSelectMultiple, help_text="What events will you bring the seed to?")
	more_info = forms.BooleanField(label="More Information", required=False, help_text="Do you want to provide more detailed information?")

class ExtendedGrainForm(SeedNetworkBaseForm):
	grain_subcategory=forms.ChoiceField(choices=GRAIN_SUBCATEGORIES,required=False)
	breed =forms.ChoiceField(choices=(('-','-'),('landrace','Landrace'),('cultivar','Cultivar')),required=False)
	plant_timing=forms.ChoiceField(choices=(('-','-'),('spring','Spring'),('fall','Fall'),('faculative','Faculative')),required=False)
        lodging=forms.ChoiceField(choices=(('-','-'),('root','Root'),('stem','Stem'),('root&stem','Root & stem')), required=False)
	lodging_percent=forms.DecimalField(max_digits=4,decimal_places=2, required=False)
	disease=forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="help text for disease")
        days_to_maturity=forms.IntegerField(required=False)
	threshing=forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="help text for threshing")
	cold_hardiness=forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="help text for cold hardiness")
	culinary_qualities=forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="help text for cooking/baking")
	other_traits=forms.CharField(label="Uses", widget=forms.Textarea(attrs={'rows':'5', 'cols':'60'}), required=False, help_text="Culinary?, Baking?, Livestock feed?, Straw for bedding?, Broom-making?, etc")
	external_url=forms.URLField(required=False)

class SeedExportForm(SeedNetworkBaseForm):
	archive = forms.BooleanField(required=False, help_text="Do you want to export your archived seed listings?")
