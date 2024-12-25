from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),

    path('records/', views.all_records, name='all_records'),
    path('records/<int:id>/', views.record_detail, name='record_detail'),

    path('manage_transaction/', views.manage_transaction, name='manage_transaction'),
    path('form/', views.handle_form, name='handle_form'),

    path('create/', views.create_ice_cream, name='create_ice_cream'),
    path('list/', views.ice_cream_list, name='ice_cream_list'),

    path('send_squares/', views.send_squares, name='send_squares'),

    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='document_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)