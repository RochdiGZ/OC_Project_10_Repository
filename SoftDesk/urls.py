"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import home
from rest_framework import routers
from projects.views import ProjectViewSet, ContributorViewSet, CommentViewSet, IssueViewSet

router = routers.DefaultRouter()
router.register(r"", ProjectViewSet, basename="projects")
router.register(r"^(?P<project_id>[^/.]+)/users", ContributorViewSet, basename="users")
router.register(r"^(?P<project_id>[^/.]+)/issues", IssueViewSet, basename="issues")
router.register(r"^(?P<project_id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentViewSet, basename="comments")

urlpatterns = [
    path('', home, name='home'),
    path('projects/', include(router.urls)),
    path('', include('users.urls')),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
