from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    # Examples:
    #url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'project_name.views.home', name='home'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+=patterns('',
         url(r'^__debug__/',include(debug_toolbar.urls)),
                          )
