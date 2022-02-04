
from django.urls import path, re_path
from .views import IndexView, AboutView, ContactView, ServiceDetailView, ServicesListView, admin_order_detail, admin_order_pdf
app_name = 'core'

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesListView.as_view(), name='services'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('admin/core/invoice/<int:invoice_id>/', admin_order_detail, name='admin_order_detail'),
    path('admin/core/invoice/<int:invoice_id>/pdf/', admin_order_pdf, name='admin_order_pdf'),
]