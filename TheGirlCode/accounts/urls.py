from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [

    #Profile
    url(r'^profile/$', views.profile , name ='profile'),

    #Login
    url(r'^login/$', login , {'template_name': 'accounts/login.html'}, name='login'),

    #Logout
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}, name='logout'),

    # Register
    url(r'^register/$', views.register, name='register'),
]