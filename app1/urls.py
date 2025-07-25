from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.all_comp, name='home'),
    path('customer/<int:pk>/',views.cust_read, name='customer'),
    path('order/<int:pk>/',views.or_read, name='order'),
    path('product/<int:pk>/',views.pr_read, name='product'),
    path('add_costumer/', views.add_customers, name='add_costumer'),
    path('add_order/', views.add_orders, name='add_order'),
    path('add_product/', views.add_products, name='add_product'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)