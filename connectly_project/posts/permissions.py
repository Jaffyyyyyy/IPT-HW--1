from rest_framework.permissions import BasePermission


class IsPostAuthor(BasePermission):
    """
    Permission check that compares post author username with authenticated user.
    Note: Post.author is posts.User model, request.user is auth.User model.
    """
    def has_object_permission(self, request, view, obj):
        # Compare usernames since Post.author is custom User model
        # and request.user is Django's auth User model
        return obj.author.username == request.user.username
