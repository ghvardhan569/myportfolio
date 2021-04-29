from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views

#Django admin header customization
admin.site.site_header = "Login to Developer Harsha"
admin.site.site_title = "Welcome to Harsha Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('certificates', views.certificates, name='certificates'),
    path('projects', views.projects, name='projects'),
    path('connect2me', views.connect2me, name='connect2me')
]
urlpatterns += staticfiles_urlpatterns()