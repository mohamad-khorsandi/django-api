from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.UserView.as_view(), name='user_list'),
    path('signup/', views.UserRegistrationView.as_view(), name='user_register'),
    path('verify/', views.UserVerifyCodeView.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),

]
