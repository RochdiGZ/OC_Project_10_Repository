# projects/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectAuthor(BasePermission):
    """
    Anyone can create a project.
    A project should only be accessible to its manager and contributors.
    """
    message = ("You do not have permission to do that."
               "Only the author can execute requests to update and delete a project.")

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author


class IsIssueAuthor(BasePermission):
    """
    Only contributors are allowed to create or read project issues.
    Only the author can execute requests to update and delete a project issue.
    """
    message = ("You do not have permissions to do that."
               "Only the author can execute requests to update and delete a project issue.")

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author


class IsCommentAuthor(BasePermission):
    """
    Only contributors are allowed to create or read issue comments.
    Only the author can execute requests to update and delete an issue comment.
    """
    message = ("You do not have permission to do that."
               "Only the author can execute requests to update and delete an issue comment.")

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
