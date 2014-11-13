from django.conf.urls import include, url, patterns
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.urls')),
)

urlpatterns += patterns("django.views",
    url(r'^media(?P<path>.*)/$',
        "static.serve", {
        "document_root": settings.MEDIA_ROOT,
    })
)