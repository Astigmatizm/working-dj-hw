from django.urls import path, re_path, register_converter
from . import views
from . import converter

register_converter(converter.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'), # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),



    # path('badrequest/', views.bad_request),
    # path('for-request/', views.forbidden_page),
    # path('found-request/', views.page_not_found),
    # path('ser-request/', views.server_error)

]
