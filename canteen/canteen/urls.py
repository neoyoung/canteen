from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

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
    # exercise
    url(r'^exercise/', include('canteen.exercise.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#exception page
handler404 = 'canteen.views.file_not_found_404'
handler500 = 'canteen.views.server_error_500'

#import pdb
#pdb.set_trace()
