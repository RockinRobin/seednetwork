from django.conf.urls import patterns, include, url
import django.contrib.auth.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
from seednetwork import settings, views, views_user
from django.views  import static
from seednetwork.forms import SeedNetworkAuthForm, SeedNetworkPasswordChangeForm

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'seednetwork.views.home', name='home'),
    url(r'^seedlibrary/', include('seedlibrary.urls')),

    url(r'^$', views.home, name='seednetwork-home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user management
    url(r'^accounts/login/$', auth.views.login, {'template_name':'login.html', 'authentication_form':SeedNetworkAuthForm}, name='auth-views-login'),
    url(r'^accounts/logout/$', auth.views.logout, {'template_name':'logout.html', 'next_page':'/'}, name='auth-views-logout'),
    url(r'^accounts/profile/$', views_user.profile, name='views_user-profile'),
    url(r'^accounts/member/(?P<mid>[0-9]+)$', views_user.member, name='views_user-member'),
    url(r'^accounts/members/$', views_user.members, name='views_user-members'),

    url(r'^accounts/profile-edit/$', views_user.edit_profile, name='views_user-edit_profile'),

    url(r'^accounts/new-user/$', views_user.new_user, name='views_user-new_user'),


    url(r'^accounts/reset-password/$', auth.views.password_reset,
		 {'template_name':'password_reset.html',
		  'email_template_name':'password_reset_email.html'}, name='password_reset'),

    url(r'^accounts/reset-password/done/$', auth.views.password_reset_done,
                {'template_name':'password_reset_done.html'},
                name='password_reset_done'),  #django hardcoded this name

    url(r'^accounts/reset-password-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
	 auth.views.password_reset_confirm, {'template_name':'password_reset_confirm.html'}, name='password_reset_confirm'),

    url(r'^accounts/reset-password-complete/$', auth.views.password_reset_complete,
		{'template_name':'password_reset_complete.html'}, name='password_reset_complete'),

    url(r'^accounts/change-password/$', auth.views.password_change,
		 {'template_name':'password_change.html', 'password_change_form':SeedNetworkPasswordChangeForm}, name='password_change'),

    url(r'^accounts/change-password/done/$', auth.views.password_change_done,
		 {'template_name':'password_change_done.html'}, name='password_change_done'),
]

if not settings.DEBUG:
	urlpatterns += [
	    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static-serve'),
	               ]
