from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("project", views.project, name="project"),
    # path("blog", views.blog, name = "blog"),
    path("test", views.PostList.as_view(), name='test'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]