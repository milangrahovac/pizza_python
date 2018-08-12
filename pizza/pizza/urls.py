# posts/urls.py
from django.urls import path


from . import views

urlpatterns = [
    #path('', views.PostList.as_view()),
    #path('<int:pk>/', views.PostDetail.as_view()),
    path('orders/', views.OrdersList.as_view()),
    path('orders/<int:pk>/', views.OrdersDetail.as_view()),
    #path('orders/', views.OrdersDetail.as_view()),
    #path('оrders/', include('pizza.urls')),
    #path('orders/<int:pk>/', ),
    #path(users/<int:pk>/orders)
]