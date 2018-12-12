from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),


    path('book_list/', views.book_list, name='book_list'),
    path('<int:id>/<slug:slug>/', views.book_detail, name='book_detail'),
    path('<int:service_id>/', views.book_share, name='book_share'),


    # services
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Rent Books
    path('RentBooks', views.RentBooks, name='RentBooks'),

    # Contact Us
    path('contactus', views.contactus, name='contactus'),
    # faq
    path('faq', views.faq, name='faq'),


]
