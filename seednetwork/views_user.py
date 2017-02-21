from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from seednetwork.forms import MemberInfoForm
from seednetwork.models import MemberInfo
from seedlibrary.models import Seed

def get_memberinfo(u):
	mi_list = MemberInfo.objects.filter(user=u)
	mi = None
	if mi_list.count() == 0:
		mi = MemberInfo.objects.create(user=u)
		mi.save()
	else:
		mi = mi_list[0];

	return mi

def fill_member_from_form(mi, form):
	mi.usda_zone = form.cleaned_data['usda_zone']
	mi.email_is_public = form.cleaned_data['email_is_public']
	mi.phone = form.cleaned_data['phone']
	mi.phone_is_public = form.cleaned_data['phone_is_public']
        country_code = form.cleaned_data['country_code']
        if country_code == "US":
                mi.street_address = '~ '.join([form.cleaned_data['street_line'],form.cleaned_data['state'], form.cleaned_data['zipcode'], country_code])
        else:
                mi.street_address = 'International address~ ' + country_code
	mi.street_address_is_public = form.cleaned_data['street_address_is_public']
	mi.mailing_address = form.cleaned_data['mailing_address']
	mi.mailing_address_is_public = form.cleaned_data['mailing_address_is_public']
	mi.about_me = form.cleaned_data['about_me']
	mi.include_in_member_profiles = form.cleaned_data['include_in_member_profiles']

def new_user(request):

	if request.method == 'POST':
		miform = MemberInfoForm(request.POST)
		uiform = UserCreationForm(request.POST)
		if miform.is_valid() and uiform.is_valid():
			user = User.objects.create_user(
				uiform.cleaned_data['username'],
				miform.cleaned_data['email'],
			    uiform.cleaned_data['password1'],
			    first_name = miform.cleaned_data['first_name'],
			    last_name = miform.cleaned_data['last_name'],
			    )
			user.save()

			mi = MemberInfo.objects.create(user=user)
			fill_member_from_form(mi, miform)
			mi.save()
			authuser = authenticate(username=user.username, password=uiform.cleaned_data['password1'])
			if authuser is not None:
				if authuser.is_active:
					login(request, authuser)
					return redirect('seednetwork-home')


		return render_to_response('profile-create.html',
			{ "miform": miform, "uiform": uiform },
              context_instance=RequestContext(request))

	return redirect('seednetwork-home')

@login_required
def profile(request):
	mi = get_memberinfo(request.user)

	return render_to_response('profile.html',
		{ "memberinfo": mi },
		context_instance=RequestContext(request))

@login_required
def edit_profile(request):
	user = request.user
	mi = get_memberinfo(user)
	error = None

	if request.method == 'POST':
		form = MemberInfoForm(request.POST)
		if form.is_valid():
			fill_member_from_form(mi, form)
			mi.save()

			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.save()

			return redirect('views_user-profile')
	else:
		data = {}
		data['first_name'] = user.first_name
		data['last_name'] = user.last_name
		data['usda_zone'] = mi.usda_zone
		data['email'] = user.email
		data['email_is_public'] = mi.email_is_public
		data['phone'] = mi.phone
		data['phone_is_public'] = mi.phone_is_public
                try:
                	sl,cc=mi.street_address.rsplit('~ ',1)
		except:
			sl = mi.street_address
			cc = "US"
                data['country_code']= cc
                if cc == 'US':
			try:
				sl, s, z = sl.split('~ ',2)
			except:
				sl = sl
				s = AL
				z = 11111
                	data['street_line'] = sl
                	data['state'] = s
                	data['zipcode'] = z
                else:
                        data['street_line'] = sl
		data['street_address_is_public'] = mi.street_address_is_public
		data['mailing_address'] = mi.mailing_address
		data['mailing_address_is_public'] = mi.mailing_address_is_public
		data['about_me'] = mi.about_me
		data['include_in_member_profiles'] = mi.include_in_member_profiles
		
		form = MemberInfoForm(data)

	return render_to_response('profile-edit.html',
		{ "form": form, "error": error },
        context_instance=RequestContext(request))

@login_required
def member(request, mid):
	memberinfo = get_object_or_404(MemberInfo, pk=mid)
        seed_list = Seed.objects.filter(user=mid, archived=False)
	return render_to_response('member.html',
			{ "memberinfo":memberinfo, "seed_list": seed_list },
			                  context_instance=RequestContext(request))


@login_required
def members(request):
	memberinfo_list = MemberInfo.objects.all().order_by('user__username')

	return render_to_response('members.html',
			{ "memberinfo_list":memberinfo_list },
			                  context_instance=RequestContext(request))
