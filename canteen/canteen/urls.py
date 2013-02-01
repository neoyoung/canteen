from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #bussiness logic
    url(r'^$', 'canteen.views.home', name='home'),

    url(r'^accounts/', include('canteen.accounts.urls')),

    url(r'^food/', include('canteen.food.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

   #static files
    url(r'^media/(?P<path>.+)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.PROJECT_DIR, 'media/')}),
    url(r'^static/(?P<path>.+)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.PROJECT_DIR, 'static/'),
          'show_indexes': True}),
)
