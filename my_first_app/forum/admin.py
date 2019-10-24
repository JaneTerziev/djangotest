from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return is_user_owner(request.user, obj.user)
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return is_user_owner(request.user, obj.user)
        else:
            return False


def is_user_owner(request_user, obj_user):
    return request_user == obj_user
