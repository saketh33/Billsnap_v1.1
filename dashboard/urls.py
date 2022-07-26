from django.urls import path, include
from . import views
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('customerlist/',views.customerlis,name='customerlist'),
    path('addcustomer/', views.addingcustomer, name='addcustomer'),
    path('deletecustomer/<utility_name>',views.deletecust,name='deletecustomer'),
    path('update/<int:id>', views.updaterecord, name='updaterecord'),
    path('bulkupload/', views.bulk_upload, name='bulkupload'),
    path('uploadlist/', views.uploadlis, name='uploadlist'),

]