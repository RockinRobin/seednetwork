from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from seednetwork.forms import MemberInfoForm, ModifiedUserCreationForm, ContactForm
from seednetwork import settings
from seednetwork.models import MemberInfo

def home(request):

	login_form = AuthenticationForm()
	create_user_form = ModifiedUserCreationForm()
	member_info_form = MemberInfoForm()

	return render_to_response('home.html',
			{ 'login_form': login_form,
			  'create_user_form': create_user_form,
			  'member_info_form': member_info_form
			},
			context_instance=RequestContext(request))

def contact(request):
	form_class = ContactForm
	error = None
        form = form_class()
	if request.method == 'POST':
        	form = form_class(data=request.POST)

        	if form.is_valid():
            		contact_name = request.POST.get(
                	    'contact_name'
            		, '')
            		contact_email = request.POST.get(
                	    'contact_email'
            		, '')
            		form_body = request.POST.get('body', '')

            # Email the profile with the
            # contact information
       	                template = loader.get_template('contact_template.txt')
            		context = {
                	   'contact_name': contact_name,
                	   'contact_email': contact_email,
                	   'form_body': form_body,
            		}
            		content = template.render(context)

            		email = EmailMessage(
                	    "New contact form submission",
                	    content,
               		    "Heritage and Landrace Grain Network" +'',
                	    [settings.DEFAULT_FROM_EMAIL,contact_email],
                	    headers = {'Reply-To': contact_email }
            		)
            		email.send()
			print 'hahahah'
			return redirect('seednetwork-contact_done')

	return render_to_response('contact.html', 
			{'form': form, "error": error
			},
			context_instance=RequestContext(request))
