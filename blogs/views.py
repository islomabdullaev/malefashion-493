from django.shortcuts import redirect
from django.views.generic import DetailView

from blogs.models import CommentModel, PostModel

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


def create_comment(request, post_pk):
    post = PostModel.objects.get(pk=post_pk)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        text = request.POST.get("text")
        CommentModel.objects.create(
            name=name, email=email,
            phone=phone, text=text,
            post=post
        )
    return redirect('blogs:details', pk=post_pk)