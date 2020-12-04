from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash_page, name='splash_page'),
    path('blog', views.post_list, name='post_list'),
    path('post/<str:id>/', views.post_detail, name='post_detail'),
]