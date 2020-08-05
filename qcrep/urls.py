from django.urls import path
from django.conf.urls.static import static
from .views import (
    QcreportListView, 
    QcreportDetailView, 
    QcreportCreateView, 
    QcreportUpdateView, 
    UserQcListView,
    CalendarView
)
from . import views

urlpatterns = [
    path('', views.home, name='qcrep-home'),
    path('about/', views.about, name='qcrep-about'),
    path('KPI_2020/', views.KPI_2020, name='qcrep-KPI_2020'),
    path('qcreport/', QcreportListView.as_view(), name='qcrep-qcreport_list'),
    path('qcreport/<int:pk>/', QcreportDetailView.as_view(), name='qcrep-qc_detail'),
    path('qcreport/new/', QcreportCreateView.as_view(), name='qcrep-qcreports_form'),
    path('qcreport/<int:pk>/update', QcreportUpdateView.as_view(), name='qcrep-qc_update'),
    path('user_reports/', views.user_reports, name='qcrep-user_reports'),
    path('client/', views.client, name='qcrep-client'),
    path('user_qc_list/<str:username>/', UserQcListView.as_view(), name='user-user_qc_list'),
    path('calendar/', CalendarView.as_view(), name='qcrep-calendar'),
]