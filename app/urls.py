"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from cars.views import  NewCarListView,CarListView,CarDetailView,CarUpdateView,CarDeleteView
from accounts.views import register_view, login_view,logout_view

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_view, name='register_view'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/',CarListView.as_view(),name='car_views'),
    path('new_car/', NewCarListView.as_view(), name='new_car_view'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='detail'),  
    path('car/<int:pk>/update/', CarUpdateView.as_view(),name='update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(),name='delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
