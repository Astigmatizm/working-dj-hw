from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('user_info/', views.user_info, name='user_info'),
    path('form/', views.form_view, name='form_view'),

    path('records/', views.all_records, name='all_records'),
    path('records/<int:id>/', views.record_detail, name='record_detail'),

    # path('send_squares/', views.send_squares, name='send_squares'),
]
