# projects/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

TYPE = (("Back-End", "Back-End"), ("Front-End", "Front-End"), ("IOS", "IOS"), ("Android", "Android"))

ROLE = (("Author", "Author"), ("Contributor", "Contributor"))
PERMISSION = (("All", "All"), ("Restricted", "Restricted"))

TAG = (("Bug", "Bug"), ("Improvement", "Improvement"), ("Task", "Task"))
PRIORITY = (("High", "High"), ("Medium", "Medium"), ("Low", "Low"))
STATUS = (("ToDo", "ToDo"), ("InProgress", "InProgress"), ("Done", "Done"))


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=10, choices=TYPE, default="Back-End")
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='project_author')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['author', 'title'], name='unique_author')]
        verbose_name = 'Project'

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_contributor')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE,
                                related_name='project_contributors')
    permission = models.CharField(max_length=12, choices=PERMISSION, default='Restricted')
    role = models.CharField(max_length=12, choices=ROLE, default='Contributor')

    class Meta:
        verbose_name = 'Contributor'
        unique_together = ['user', 'project']

    def __str__(self):
        if self.role == "Author":
            return f"{self.role} : {self.user}"
        return f"{self.user}"


class Issue(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=2500)
    tag = models.CharField(max_length=12, choices=TAG)
    priority = models.CharField(max_length=12, choices=PRIORITY)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='issue_related')
    status = models.CharField(max_length=12, choices=STATUS, default='ToDo')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='issue_author')
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 related_name='issue_assigned_to')
    # created_time = models.DateTimeField(default=timezone.now, editable=False)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Issue'

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=500, blank=False, unique=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='comment_author')
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE,
                              related_name='issue_comment')
    # created_time = models.DateTimeField(default=timezone.now, editable=False)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Comment'

    def __str__(self):
        return str(self.description)
