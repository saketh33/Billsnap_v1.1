from django.urls import path, include
from . import views
from django.contrib.auth import views as a_views

urlpatterns = [
    path('addapp/', views.addapp, name='addapp'),
    path('all/', views.showapps, name='showapps'),
    path('deleteapp/<aslug>',views.deleteapp,name='deleteapp'),
    path('<slug>/', include('dashboard.urls')),
]