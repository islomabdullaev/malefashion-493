from django.shortcuts import render
from django.views.generic import DetailView

from blogs.models import PostModel

# Create your views here.

# DetailView CBV
class BlogDetailView(DetailView):
    template_name = "blog-details.html"
    model = PostModel
    context_object_name = "post"


# Detail View FBV
# def blog_detail_view(request, pk):
#     post = PostModel.objects.get(pk=pk)
#     context = {
#         "post": post
#     }
#     return render(request, template_name="blog-details.html", context=context)