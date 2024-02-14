from django.urls import path
from blogs.views import BlogDetailView, create_comment

app_name = 'blogs'

urlpatterns = [
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="details"),
    path('posts/<int:post_pk>/comment/', create_comment, name="create_comment")
]
