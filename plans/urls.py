from django.urls import path, include
from . import views
from .views import *
from django.contrib.auth import views as a_views

urlpatterns = [
    path('subscribe-plan/<str:slug>', subscribe, name='subscribe-plan'),
    path('upgrade-to/<str:slug>', upgrade_to, name='upgrade-to'),
    path('', plans_panel, name='plans-panel'),
    path('delete-plan/<str:slug>', delete_plan, name='delete-plan'),
    path('plan/<str:slug>', show_plan, name='plan'),
    path('update-plan/<str:slug>', update_user_plan, name='update-plan'),
]
