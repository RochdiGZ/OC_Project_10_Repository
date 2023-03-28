from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author_user_id']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        read_only_fields = ['project_id', 'permission', 'role']


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ['project_id', 'author_user_id']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['issue_id', 'author_user_id']
