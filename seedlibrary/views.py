# Seed library views
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from seedlibrary.forms import GrainForm, SeedExportForm, ExtendedGrainForm
from seedlibrary.models import Seed, Event, ExtendedView

from datetime import datetime, timedelta

# For rendering seed lists in CSV format
import csv
from django.http import HttpResponse

def home(request):
	return render_to_response('seedlib-home.html',
		{},
		context_instance=RequestContext(request))

def update_seed_events(seed, all_checked_events):
	all_events = Event.objects.filter(show_on_seed_edit=True)
	for e in all_events:
		if e in all_checked_events:
			e.seed.add(seed)
		else:
			e.seed.remove(seed)



@login_required
def seed_create(request):
	seed_form = GrainForm()
	seed_form_extended = ExtendedGrainForm()  
	if request.method == 'POST':
		seed_form = GrainForm(request.POST)
                seed_form_extended = ExtendedGrainForm(request.POST)
		if seed_form.is_valid():

			seed = Seed.objects.create(
				user = request.user,
				seed_type = 'grain',
				crop_type = seed_form.cleaned_data['crop_type'],
                                grain_subcategory = seed_form.cleaned_data['grain_subcategory'],
				seed_variety = seed_form.cleaned_data['seed_variety'],
				seed_description = seed_form.cleaned_data['seed_description'],
				enough_to_share = seed_form.cleaned_data['enough_to_share'],
				year = seed_form.cleaned_data['year'],
				origin = seed_form.cleaned_data['origin'],
                                more_info = seed_form.cleaned_data['more_info']
			)
			seed.save()
                        if not seed.more_info:
                               return redirect('views-seed_create_confirm')
                
                if seed_form.is_valid() and seed.more_info and seed_form_extended.is_valid():
                        extended_seed = ExtendedView.objects.create(
                                parent_seed = seed,
				latin_name = seed_form_extended.cleaned_data['latin_name'],
                                improvement_status = seed_form_extended.cleaned_data['improvement_status'],
                                growth_habit = seed_form_extended.cleaned_data['growth_habit'],
                                lodging = seed_form_extended.cleaned_data['lodging'],
                                cultivation = seed_form_extended.cleaned_data['cultivation'],
                                disease = seed_form_extended.cleaned_data['disease'],
                                days_to_maturity = seed_form_extended.cleaned_data['days_to_maturity'],
                                threshing = seed_form_extended.cleaned_data['threshing'],
                                cold_hardiness = seed_form_extended.cleaned_data['cold_hardiness'],
                                culinary_qualities = seed_form_extended.cleaned_data['culinary_qualities'],
                                other_uses = seed_form_extended.cleaned_data['other_uses'],
                                additional_info = seed_form_extended.cleaned_data['additional_info'],
                                external_url = seed_form_extended.cleaned_data['external_url']
                        )

                        extended_seed.save()

                        
#			update_seed_events(seed, seed_form.cleaned_data['events'])

			return redirect('views-seed_create_confirm')
		

	return render_to_response('seed-create.html',
		{"seed_form":seed_form,"seed_form_extended":seed_form_extended},
		context_instance=RequestContext(request))
	


@login_required
def seed_create_confirm(request):
	return render_to_response('seed-confirm.html',
		{},
		context_instance=RequestContext(request))

        
@login_required
def seeds(request):  
	seed_list = Seed.objects.filter(user=request.user, archived=False).order_by('crop_type', 'grain_subcategory', 'seed_variety')
	seed_archive_list = Seed.objects.filter(user=request.user, archived=True)

	return render_to_response('seeds.html',
		{ "seed_list": seed_list, "seed_archive_list": seed_archive_list },
		context_instance=RequestContext(request))

def fill_seed_from_form(seed, form):
#	seed.seed_type = form.cleaned_data['seed_type']
	seed.crop_type = form.cleaned_data['crop_type']
        seed.grain_subcategory = form.cleaned_data['grain_subcategory']
	seed.seed_variety = form.cleaned_data['seed_variety']
	seed.seed_description = form.cleaned_data['seed_description']
	seed.enough_to_share = form.cleaned_data['enough_to_share']
	seed.year = form.cleaned_data['year']
	seed.origin = form.cleaned_data['origin']
        seed.more_info = form.cleaned_data['more_info']

def fill_ev_from_evform(extended_view, evform):
	extended_view.latin_name = evform.cleaned_data['latin_name']
        extended_view.improvement_status = evform.cleaned_data['improvement_status']
        extended_view.growth_habit = evform.cleaned_data['growth_habit']
        extended_view.lodging = evform.cleaned_data['lodging']
        extended_view.cultivation = evform.cleaned_data['cultivation']
        extended_view.disease = evform.cleaned_data['disease']
        extended_view.days_to_maturity = evform.cleaned_data['days_to_maturity']
        extended_view.threshing = evform.cleaned_data['threshing']
        extended_view.cold_hardiness = evform.cleaned_data['cold_hardiness']
        extended_view.culinary_qualities = evform.cleaned_data['culinary_qualities']
        extended_view.other_uses = evform.cleaned_data['other_uses']
        extended_view.additional_info = evform.cleaned_data['additional_info']
        extended_view.external_url = evform.cleaned_data['external_url']


@login_required
def seed_export(request):
	seed_export_form = SeedExportForm()
	if request.method == 'POST':
		seed_export_form = SeedExportForm(request.POST)
		if seed_export_form.is_valid():
			try:
				request.POST['archive']
			except:
				include_archived = False
			else:
				include_archived = True
			seed_list = Seed.objects.filter(user=request.user, archived=include_archived)
			return seeds_as_csv_to_response(seed_list)

	return render_to_response('seed-export.html',
			{"seed_export_form":seed_export_form},
			context_instance=RequestContext(request))

def seeds_as_csv_to_response(seed_list):
	response = HttpResponse(content_type='text/csv')
	writer = csv.writer(response)
	# Write header row.
	writer.writerow([
		'Title',
		'Type',
		'Quantity',
		'Common Name',
		'Unit label',
		'Seed Expiration Date',
		'Exchange Expiration Date',
		'Notes',
		'Scientific Name'
		])
	for seed in seed_list:
		title = ' '.join(seed.seed_description.split(' ')[:10])
		type = 'Give' if seed.enough_to_share else 'Get'
		quantity = ''
		common_name = seed.crop_type
		unit = 'Packets'
		seed_expiry_date = ''
		exchange_expiry_date = datetime.now() + timedelta(days=365)
		notes = seed.seed_description
		scientific_name = seed.seed_variety
		writer.writerow([
			title,
			type,
			quantity,
			common_name,
			unit,
			seed_expiry_date,
			exchange_expiry_date.isoformat(),
			notes,
			scientific_name
			])

	return response

@login_required
def seed_edit(request, id):
	seed = get_object_or_404(Seed, pk=id)
        try:
                extended_view = seed.extendedview_set.get()
        except:
                extended_view = ExtendedView(parent_seed = seed)

	error = None

	if request.method == 'POST':
		form = GrainForm(request.POST)
		extended_form=ExtendedGrainForm(request.POST)
		if form.is_valid():
			fill_seed_from_form(seed, form)
			seed.save()
                if extended_form.is_valid():
			fill_ev_from_evform(extended_view, extended_form)
                        extended_view.save()
                if not seed.more_info and len(seed.extendedview_set.all()) != 0:
                        extended_view.delete()
#			update_seed_events(seed, form.cleaned_data['events'])
                if form.is_valid() and extended_form.is_valid():
			return redirect('views-seeds')
	else:
		data = {}
		data['seed_type'] = seed.seed_type
		data['crop_type'] = seed.crop_type
                data['grain_subcategory'] = seed.grain_subcategory
		data['seed_variety'] = seed.seed_variety
		data['seed_description'] = seed.seed_description
		data['enough_to_share'] = seed.enough_to_share
		data['year'] = seed.year
		data['origin'] = seed.origin
                data['more_info'] = seed.more_info
                if seed.more_info:
		       data['latin_name']=extended_view.latin_name
                       data['improvement_status']=extended_view.improvement_status
                       data['growth_habit']=extended_view.growth_habit
                       data['lodging']=extended_view.lodging
                       data['cultivation']=extended_view.cultivation
                       data['disease']=extended_view.disease
                       data['days_to_maturity']=extended_view.days_to_maturity
                       data['threshing']=extended_view.threshing
                       data['cold_hardiness']=extended_view.cold_hardiness
                       data['culinary_qualities']=extended_view.culinary_qualities
                       data['other_uses']=extended_view.other_uses
                       data['additional_info']=extended_view.additional_info
                       data['external_url']=extended_view.external_url
		e_ids = []
		for e in seed.event_set.all():
			e_ids.append(e.id)
		data['events'] = e_ids

		form = GrainForm(data)
		extended_form = ExtendedGrainForm(data)

	return render_to_response('seed-edit.html',
		{ "seed":seed, "form": form, "extended_form": extended_form, "error": error },
        context_instance=RequestContext(request))

@login_required
def seed_confirm_archive(request, id):
	seed = get_object_or_404(Seed, pk=id, user=request.user)
	error = None

	if request.method == 'POST':
		if request.POST['command'] == 'archive' and not seed.archived:
			seed.archived = True
			seed.save()
		elif request.POST['command'] == 'unarchive' and seed.archived:
			seed.archived = False
			seed.save()

		return redirect('views-seeds')

	return render_to_response('seed-confirm-archive.html',
			{ "seed":seed, "error": error },
			context_instance=RequestContext(request))

login_required
def seed_confirm_delete(request, id):
        seed = get_object_or_404(Seed, pk=id, user=request.user)
        error = None

        if request.method == 'POST':
                if request.POST['command'] == 'delete':
                        instance = Seed.objects.get(id=id)
                        instance.delete()

                return redirect('views-seeds')

        return render_to_response('seed-confirm-delete.html',
                        { "seed":seed, "error": error },
                        context_instance=RequestContext(request))

@login_required
def seed_profile(request, id):
	seed = get_object_or_404(Seed, pk=id)
        try:
                extended_view = seed.extendedview_set.get()
        except:
                extended_view = ExtendedView(parent_seed = seed)
                extended_view.save()
        return render_to_response('seed-profile.html',
                        {"seed":seed, "ev": extended_view},
                        context_instance=RequestContext(request))










@login_required
def events(request):
	yesterday = datetime.now() - timedelta(days=1)
	event_list = Event.objects.filter(date__gte=yesterday).order_by('date')
	past_event_list = Event.objects.filte(date__lt=yesterday).order_by('-date')

	return render_to_response('events.html',
			{ "event_list": event_list, "past_event_list":past_event_list},
            context_instance=RequestContext(request))

@login_required
def seeds_at_event(request, id):
	event = get_object_or_404(Event, pk=id)

	seed_list = event.seed.all()

	return render_to_response('seeds-at-event.html',
			{ "seed_list": seed_list, "event": event },
			                  context_instance=RequestContext(request))
