# projects/permissions.py
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Contributor, Project


class ProjectPermission(BasePermission):
    message = "A project should only be accessible to its author and contributors."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        if request.method in ['PUT', 'DELETE']:
            return request.user == obj.author


class ContributorPermission(BasePermission):
    message = "A project should only be accessible to its author and contributors."

    def has_object_permission(self, request, view, obj):
        if Project.objects.filter(projet=view.kwargs['project_pk']).exists():
            if request.method in SAFE_METHODS:
                return True
            if request.method in ['POST', 'PUT', 'DELETE']:
                self.message = "Only the author can execute requests to add, update or delete a project contributor."
                return Contributor.objects.filter(project=view.kwargs['project_pk'], user=request.user,
                                                  role="Author", permission="All").exists()
        self.message = "This project does not exist"
        return False


class IssuePermission(BasePermission):
    message = "Only contributors are allowed to create or read project issues."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        if request.method in ['PUT', 'DELETE']:
            self.message = "Only the author can execute requests to update and delete a project issue."
            return request.user == obj.author


class CommentPermission(BasePermission):
    message = "Only contributors are allowed to create or read issue comments."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        if request.method in ['PUT', 'DELETE']:
            self.message = "Only the author can execute requests to update and delete an issue comment."
            return request.user == obj.author
