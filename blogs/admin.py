from django.contrib import admin

from blogs.models import AuthorModel, PostModel, CommentModel

# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)