from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
<<<<<<< HEAD
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('like/<int:post_id>/', views.LikeView, name='like_post'),
=======
>>>>>>> bba7967e0142db0b2effb0b7ccb28e53f831396b
]