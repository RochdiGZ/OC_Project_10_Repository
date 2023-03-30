from django.utils import timezone
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    project_contributors = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ["id",
                  "project_contributors",
                  "title",
                  "description",
                  "type",
                  "created_at",
                  "author",
                  "issue_related", ]
        extra_kwargs = {
            'author': {'read_only': True},
            'created_at': {'default': timezone.now, 'format': '%d %B %Y %H:%M'}
        }


class ContributorSerializer(ModelSerializer):
    class Meta(object):
        model = Contributor
        fields = "__all__"
        # read_only_fields = ['project', 'permission', 'role']
        extra_kwargs = {
            'project': {'read_only': True},
            'permission': {'read_only': True},
            'role': {'read_only': True},
            'created_time': {'default': timezone.now, 'format': '%d %B %Y %H:%M'},
            'last_updated': {'default': timezone.now, 'format': '%d %B %Y %H:%M'}
        }


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
        # read_only_fields = ['project', 'author']
        extra_kwargs = {
            'project': {'read_only': True},
            'author': {'read_only': True},
            'created_time': {'default': timezone.now, 'format': '%d %B %Y %H:%M'},
            'last_updated': {'default': timezone.now, 'format': '%d %B %Y %H:%M'}
        }


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # read_only_fields = ['issue', 'author']
        extra_kwargs = {
            'issue': {'read_only': True},
            'author': {'read_only': True},
            'created_time': {'default': timezone.now, 'format': '%d %B %Y %H:%M'},
            'last_updated': {'default': timezone.now, 'format': '%d %B %Y %H:%M'}
        }
