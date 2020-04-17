from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, CarCreateView



urlpatterns = [
    path('',views.home, name ='home'),
    path('post/<int:pk>/', views.post_detail_with_comment, name ='post_detail_with_comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name ='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('car/new/', CarCreateView.as_view(), name='car-create'),
    path('search/',views.search, name='search')
]