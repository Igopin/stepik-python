from django.urls import path
from qa import views

urlpatterns = [
    path('',         views.test),
    path('login/',   views.login),
    path('signup/',  views.test),
    path('ask/',     views.test),
    path('popular/', views.test),
    path('new/',     views.test),
    path('question/<int:question_id>/', views.question)
]
