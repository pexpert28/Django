from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^login/$', login, name="login"),
    url(r'^profile/$', login_required(views.profile), name='profile'),
    url(r'^createGroup/$', login_required(views.CreateGroup.as_view()), name='createGroup'),
]
