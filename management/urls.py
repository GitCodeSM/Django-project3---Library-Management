from django.urls import path

from management import views

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]
