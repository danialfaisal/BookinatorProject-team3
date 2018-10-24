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

    # customer
    #path('customer_list', views.customer_list, name='customer_list'),
    #path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    #path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    #path('customer/<int:pk>/summary/', views.summary, name='summary'),

    # services
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # products
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),


]
