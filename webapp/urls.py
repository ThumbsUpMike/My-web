from django.urls import path
from .views import home, contact, contact_list, contact_details, contact_delete, resume

app_name = "webapp"

urlpatterns = [
    path('', home, name='home'),
    path('contact/list', contact_list, name='contact_list'),
    path('<int:pk>/', contact_details, name='contact_details'),
    path('<int:pk>/delete/', contact_delete, name='contact_delete'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
]