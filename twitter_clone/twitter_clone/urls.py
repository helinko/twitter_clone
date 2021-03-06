from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from MyAuth.forms import MyUserForm

urlpatterns = [
    # Examples:
    # url(r'^$', 'twitter_clone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index', name='index'),
    url(r'^user/([A-Za-z0-9_]+)/$', 'main.views.profile', name='profile'),
    url(r'^logout/', 'main.views.logout_view', name='logout_view'),
    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=MyUserForm),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
