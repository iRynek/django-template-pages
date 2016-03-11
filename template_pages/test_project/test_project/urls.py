from django.conf.urls import include, url


urlpatterns = [
    url(ur'^', include('template_pages.urls')),
]

