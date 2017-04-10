from django.conf.urls import patterns, include, url

from seedlibrary import views, views_search

urlpatterns = [
	url(r'^$', views.home, name='seedlibrary-home'),
	url(r'^seeds/create/$', views.seed_create, name='views-seed_create'),
	url(r'^seeds/create-confirm/$', views.seed_create_confirm, name='views-seed_create_confirm'),
	url(r'^seeds/$', views.seeds, name='views-seeds'),
	url(r'^seeds/export/$', views.seed_export, name='views-seed_export'),
	url(r'^seeds/edit/(?P<id>[0-9]+)$', views.seed_edit, name='views-seed_edit'),
	url(r'^seeds/confirm-archive/(?P<id>[0-9]+)$', views.seed_confirm_archive, name='views-seed_confirm_archive'),
	url(r'^seeds/confirm-delete/(?P<id>[0-9]+)$', views.seed_confirm_delete, name='views-seed_confirm_delete'),
	url(r'^seeds/seed-profile/(?P<id>[0-9]+)$', views.seed_profile, name='views-seed_profile'),
	url(r'^search/$', views_search.seed_search, name='views_search-seed_search'),
	url(r'^events/$', views.events, name='views-events'),
	url(r'^seeds-at-event/(?P<id>[0-9]+)$', views.seeds_at_event, name='views-seeds_at_event'),
]


