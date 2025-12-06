from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    comment_create,
    CategoryListView, CategoryDetailView,
    SignUpView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/novo/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/remover/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comentarios/novo/', comment_create, name='comment-create'),
    path('categorias/', CategoryListView.as_view(), name='category-list'),
    path('categorias/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
     path('accounts/signup/', SignUpView.as_view(), name='signup'),
]
