# projects/permissions.py
from django.http import Http404
from rest_framework.permissions import BasePermission
from .models import Contributor


class IsAuthor(BasePermission):
    """
    Contributors can List other contributors, Read details about them
    Authors can List, Read, Add, Update or Delete a contributor
    """
    message = "You do not have permission to do that."

    def has_permission(self, request, view):
        current_project = view.kwargs.get('project_id')
        if Contributor.objects.filter(project=current_project).exists():
            return Contributor.objects.filter(project=current_project, user=request.user,
                                              role="Author", permission="All").exists()
        raise Http404()


class IsManager(BasePermission):
    """
    Anyone can create a project.
    Contributors can List theirs projects, Read a project
    Authors can Create, Read, Update and Delete a project.
    """
    message = "You do not have permissions to do that."

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            current_project = view.get_project()
            contributors = Contributor.objects.filter(project=current_project)
            return contributors.filter(user=request.user).exists()
        if view.action in ['update', 'destroy']:
            return request.user == obj.author


class IsContributor(BasePermission):
    """
    Project contributors can List all project issues and comments, Create or Read an issue or a comment.
    Issue author or Comment author can Update and Delete their issues or comments.
    """
    message = "You do not have permission to do that."

    def has_permission(self, request, view):
        if view.get_project():
            current_project = view.kwargs.get('project_id')
            contributors = Contributor.objects.filter(project=current_project)
            return contributors.filter(user=request.user).exists()
        raise Http404()

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'create', 'retrieve']:
            current_project = view.get_project()
            contributors = Contributor.objects.filter(project=current_project)
            return contributors.filter(user=request.user).exists()
        if view.action in ['update', 'destroy']:
            return request.user == obj.author
