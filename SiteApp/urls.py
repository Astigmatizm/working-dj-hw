from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),

    path('form/', views.form_view, name='form_view'),

    path('records/', views.all_records, name='all_records'),
    path('records/<int:id>/', views.record_detail, name='record_detail'),

    path('send_squares/', views.send_squares, name='send_squares'),
]
