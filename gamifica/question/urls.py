from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createQuestion, name='create_question'),
    path('edit/<int:id>/', views.editQuestion, name='edit_question'),
    path('delete/<int:id>/', views.deleteQuestion, name='delete_question'),
    path('list/', views.listQuestions, name='list_questions'),
    path('list/all/', views.listAllQuestion, name='list_all_questions'),
    path('view/<int:id>/', views.viewQuestion, name='view_question'),
    path('dinamica/', views.dinamica, name='check_answer'),
]