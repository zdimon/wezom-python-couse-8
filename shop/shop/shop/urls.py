"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from main.views import index, about, detail, filter, signin, logout, registration, profile
from shop.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('rosetta/', include('rosetta.urls')),
    path('about', about),
    path('signin', signin),
    path('logout', logout),
    path('registration', registration),
    path('profile', profile),
    path('detail/<int:index>', detail, name="detail"),
    path('filter/<int:category_id>', filter, name="filter"),
    path('admin/', admin.site.urls),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += i18n_patterns(
        path('', index)
)