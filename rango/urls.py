from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category')
]
=======
    path('about/', views.about, name='about')
]
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
