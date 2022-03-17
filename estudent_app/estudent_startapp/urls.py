from unicodedata import name
from django.urls import path 
from django.urls import include
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import getHomepageData
from django.conf.urls import url

#URL Config
urlpatterns = [
    path('administrator/', admin.site.urls),
    path('landingprototype/', views.landingprototype),
    path('style/', views.style),
    path('landing/', views.landing, name = 'landing'),
    path('homepage/', views.homepage, name = 'home'),
    path('landing/', views.landing, name = 'logout'),
    path('newstyle/', views.newstyle),
    path('goals/', views.goals),
    path('info/', views.information, name = 'info'),
    path('profile/', views.profile, name = 'profile'),
    path('about/',views.about),
    path('termsandconditions/', views.termsandconditions),
    path('oldhomepage/', views.oldhomepage),
    path('pagesstyle/', views.pagesstyle),
    path('', include("django.contrib.auth.urls")),
    path('chart/', views.chart, name = 'chart'),
    url(r'^api/data/', getHomepageData, name='api-data'),
    path('export_to_csv/', views.export_to_csv, name='export_to_csv')
]

urlpatterns += staticfiles_urlpatterns()

