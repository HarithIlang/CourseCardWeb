from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('today/', views.today_page, name='today'),
    path('courses/', views.courses_page, name='courses'),
    path('courses/<int:course_id>/', views.course_details_page, name='course_details'),
    path('calendar/', views.calendar_page, name='calendar'),
]