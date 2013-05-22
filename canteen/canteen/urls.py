from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('canteen.foods.urls')),

    url(r'^accounts/', include('canteen.accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Order API
    url(r'^order/', include('canteen.order.urls')),
)

#exception page
handler404 = 'canteen.views.file_not_found_404'
handler500 = 'canteen.views.server_error_500'
