from django.conf.urls import patterns
from django.conf.urls import url
from apps.accounts.views import *

urlpatterns = patterns("apps.accounts.views",
		url(r'^$',HomePage.as_view(), name='home'),
		url(r'^login/$','user_login',name='login'),
		url(r'^register/$','register', name='register'),
		url(r'^campground/create$',CreateCampgroundView.as_view(), name='create_campground_view'),
		)
