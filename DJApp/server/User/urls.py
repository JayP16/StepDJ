from django.conf.urls import url
from User import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('login/$',auth_views.login,{'template_name':'login.html'}) ,
    url('logout/',auth_views.logout,{'next_page':'/'}),
]
