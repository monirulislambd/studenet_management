from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='student_list'),
    path('home/', views.home, name='home'),
    path('individual_information/<int:id>', views.individual_information, name='individual_information'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
]
