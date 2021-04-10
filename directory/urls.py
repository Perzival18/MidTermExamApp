from django.urls import path
from . import views

app_name = 'directory'

urlpatterns = [
 path('', views.home, name='home'),
 path('students/', views.all_students, name='all_students'),
 path('students/<int:student_id>/', views.student, name='student'),
 path('teachers/', views.all_teachers, name='all_teachers'),
 path('teachers/<int:teacher_id>/', views.teacher, name='teacher'),

]