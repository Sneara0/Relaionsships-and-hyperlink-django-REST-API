from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns( [
   
       path('myapi/', views.BlogList.as_view()),
       path('snedetail/<int:pk>/', views.apiDetail.as_view()),
       path('gav/', views.contactList.as_view(),name='contact-list'),
       path('', views.api_root),
   
    

          
])