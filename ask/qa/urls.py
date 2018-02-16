from django.urls import path
from qa import views

urlpatterns = [
    path('',         views.questions_new),
    path('popular/', views.questions_popular),
    path('question/<int:question_id>/', views.show_question, name="qa-question"),
    path('login/',   views.login),
    path('signup/',  views.test),
    path('ask/',     views.test),
    path('new/',     views.test)
]
