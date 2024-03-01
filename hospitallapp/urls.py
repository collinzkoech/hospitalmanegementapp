
from django.contrib import admin
from django.urls import path
from hospitallapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('innerpage/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('details/', views.detail, name='detail'),
    path('users/', views.user, name='user'),
    path('adminhome/', views.adminhome, name='adminhome'),

]
