from django.conf.urls import patterns, include, url

from seedlibrary import views, views_search

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^seeds/create/$', views.seed_create),
	url(r'^seeds/create-confirm/$', views.seed_create_confirm),
	url(r'^seeds/$', views.seeds),
	url(r'^seeds/export/$', views.seed_export),
	url(r'^seeds/edit/(?P<id>[0-9]+)$', views.seed_edit),
	url(r'^seeds/confirm-archive/(?P<id>[0-9]+)$', views.seed_confirm_archive),
	url(r'^search/$', views_search.seed_search),
	url(r'^events/$', views.events),
	url(r'^seeds-at-event/(?P<id>[0-9]+)$', views.seeds_at_event),
]


