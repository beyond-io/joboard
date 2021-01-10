from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from joboard_home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('showDetails/', views.show_details, name='showDetails'),
    url(r'^notification/', include('user_notification.urls'), name="notification"),
    path('', views.home_page, name='home_page'),
    url(r'^accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^jobs/', include('search_job.urls')),
]
