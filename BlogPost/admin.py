from django.contrib import admin
from .models import *

# Register your models here.
from BlogPost.models import Publication


class UserModelAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(UserModel, UserModelAdmin)


class PublicationAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.user == request.user:
            return True
        return False

    def has_add_permission(self, request):
        return True

    def get_queryset(self, request):
        blocker_user = BlockedUsers.objects.filter(blocked_user=request.user).values_list("blocker")
        queryset = super(PublicationAdmin, self).get_queryset(request)
        return queryset.exclude(user__in=blocker_user)


admin.site.register(Publication, PublicationAdmin)


class CommentOnPublicationAdmin(admin.StackedInline):
    model = CommentOnPublication
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentOnPublicationAdmin, ]

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.user == request.user:
            return True
        return False

    def get_queryset(self, request):
        blocker_user = BlockedUsers.objects.filter(blocked_user=request.user).values_list("blocker")
        queryset = super(CommentAdmin, self).get_queryset(request)
        return queryset.exclude(user__in=blocker_user)


admin.site.register(Comment, CommentAdmin)


class BlockedUsersAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj is not None and obj.blocker == request.user:
            return True
        return False

    def get_queryset(self, request):
        blocker_user = BlockedUsers.objects.filter(blocked_user=request.user).values_list("blocker")
        queryset = super(BlockedUsersAdmin, self).get_queryset(request)
        return queryset.exclude(blocker__in=blocker_user)


admin.site.register(BlockedUsers, BlockedUsersAdmin)
