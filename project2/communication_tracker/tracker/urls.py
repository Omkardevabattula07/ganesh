# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('log/<int:company_id>/', views.log_communication, name='log_communication'),
#     path('calendar/', views.calendar_page, name='calendar_page'),
#     path('calendar/events/', views.calendar_view, name='calendar_events'),
#     path('analytics/', views.analytics_page, name='analytics_page'),
#     path('analytics/data/', views.analytics_view, name='analytics_data'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar_page, name='calendar_page'),
    path('analytics/', views.analytics_page, name='analytics_page'),
    path('upload/', views.upload_page, name='upload_page'),
]
