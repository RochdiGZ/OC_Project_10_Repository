# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
# from .permissions import IsAuthor, IsManager, IsContributor


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Create, Retrieve, Update and Delete a project.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_project(self):
        current_project = self.kwargs["project_pk"]
        return get_object_or_404(Project, id=current_project)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=request.user, project=project, role="Author", permission="All")
        return Response({
            'project': ProjectSerializer(project, context=self.get_serializer_context()).data,
            'message': "The project has been created successfully"},
            status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(
                {'message': "The project has been deleted successfully"},
                status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ContributorViewSet(viewsets.ModelViewSet):
    """
    Add, Retrieve, Update and Delete a project contributor.
    """
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ retrieve all contributors of a project """
        current_project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        return Contributor.objects.filter(project=current_project)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        current_project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        current_user = request.data['user']
        current_user_exist = Contributor.objects.filter(user=current_user, project=current_project)

        if current_user_exist:
            return Response({
                    "message": "This user is already a contributor for this project."},
                    status=status.HTTP_403_FORBIDDEN)
        else:
            serializer.is_valid(raise_exception=True)
            contribution = serializer.save(project=current_project)
            return Response({'contribution': ContributorSerializer(contribution,
                            context=self.get_serializer_context()).data,
                            'message':
                            f"This new contributor has been successfully added to : {current_project}."},
                            status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            get_object_or_404(Project, pk=self.kwargs['project'])
            contributor_to_delete = Contributor.objects.get(
                project=self.kwargs['project'],
                user=self.kwargs['user'])

            if contributor_to_delete.role == "Author":
                return Response(
                    {'message': "The author can't be deleted."},
                    status=status.HTTP_403_FORBIDDEN)
            else:
                self.perform_destroy(contributor_to_delete)
                return Response(
                        {'message': "This contributor has been successfully deleted."},
                        status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            raise ValidationError("This contributor does not exist.")


class IssueViewSet(viewsets.ModelViewSet):
    """
    Create, Retrieve, Update and Delete a project issue.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_project(self):
        lookup_field = self.kwargs['project_pk']
        return get_object_or_404(Project, id=lookup_field)

    def get_queryset(self):
        current_project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        return Issue.objects.filter(project=current_project).order_by('-last_updated')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            current_project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
            serializer.is_valid(raise_exception=True)
            new_issue = serializer.save(author=self.request.user, project=current_project)
            return Response({
                'New issue': IssueSerializer(new_issue, context=self.get_serializer_context()).data,
                'message': f"This project issue has been successfully added to : {current_project}"},
                status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(
                {'message': "This project issue has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Create, retrieve, update and delete a comment of an issue.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_project(self):
        lookup_field = self.kwargs['project_pk']
        return get_object_or_404(Project, id=lookup_field)

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk']).order_by('-last_updated')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            current_project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
            current_issue = get_object_or_404(Issue, pk=self.kwargs['issue_pk'], project=current_project)
            if current_issue:
                serializer.is_valid(raise_exception=True)
                new_comment = serializer.save(author=self.request.user, issue=current_issue)
                return Response({
                    'New comment': CommentSerializer(new_comment, context=self.get_serializer_context()).data,
                    'message': f"This issue comment has been successfully added to : {current_issue}"},
                    status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(
                {'message': "This issue comment has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
