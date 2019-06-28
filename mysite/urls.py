"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from chat import views

urlpatterns = [
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/$', views.Reg_Form, name="user_reg"),
    url(r'^login/$', views.login_form, name="user_log"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'logout/', views.logout_form, name="logout"),
    url(r'^$', RedirectView.as_view(url='/dashboard/'))
]

