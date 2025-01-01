from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    # Dashboard URL
    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Regional sales summary URL (filtered by region)
    path('regional-sales-summary/<str:region>/', views.regional_sales_summary, name='regional_sales_summary'),

    # Dynamic sales data (Product-wise)
    path('dynamic-sales-data/', views.dynamic_sales_data, name='dynamic_sales_data'),

    # Sales comparison (Kenya Summary)
    path('regional-sales-comparison/', views.regional_sales_comparison, name='regional_sales_comparison'),
    

    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
]
