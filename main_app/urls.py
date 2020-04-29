from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.CatList.as_view(), name='cats_index'), 
    path('cats/<int:pk>', views.CatDetail.as_view(), name='cats_detail')
]
