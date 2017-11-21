from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [

    # Profile
    url(r'^profile/$', views.view_profile, name ='profile'),

    # Profile Settings
    url(r'^settings/$', views.settings_profile, name ='settings'),

    # Edit Profile Details
    url(r'^settings/edit/$', views.edit_profile, name ='edit_profile'),

    # Change Password
    url(r'^settings/edit/change_password$', views.change_password, name ='change_password'),

    # Login
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),

    # Logout
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}, name='logout'),

    # Register
    url(r'^register/$', views.register, name='register'),


]