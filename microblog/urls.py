from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.views.generic import TemplateView

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),

    # url(r"^$", TemplateView.as_view(template_name="index.html")),
    
    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r"^blog/", include("blog.urls", namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
