from django.urls import path, register_converter
from realty import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')
urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('about/', views.about, name='about'),
    path('addproject/', views.addproject, name='addproject'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]
