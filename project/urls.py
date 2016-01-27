"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from portfolio import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^$', 'portfolio.views.index'),
    url(r'^about-me-index/$', 'portfolio.views.about_me'),
    url(r'^$', 'portfolio.views.index2'),

    # Projects

    url(r'^Projects/projects/$', 'portfolio.views.projects'),
    url(r'^google/$', 'portfolio.views.google'),
    url(r'^google_search/$', 'portfolio.views.google_search'),

    url(r'^luigi/$', 'portfolio.views.luigi_bootstrap'),
    url(r'^grid/$', 'portfolio.views.color_grid'),
    url(r'^j_streetfighter/$', 'portfolio.views.jquery_fighter'),
    url(r'^landing_page/$', 'portfolio.views.landing_page'),
    
]
