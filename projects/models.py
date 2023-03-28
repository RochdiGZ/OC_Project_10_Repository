# projects/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

TYPE = (("Back-End", "Back-End"), ("Front-End", "Front-End"), ("IOS", "IOS"), ("Android", "Android"))

ROLE = (("Author", "Author"), ("Manager", "Manager"), ("Contributor", "Contributor"))
PERMISSION = (("All", "All"), ("Restricted", "Restricted"))

TAG = (("Bug", "Bug"), ("Improvement", "Improvement"), ("Task", "Task"))
PRIORITY = (("High", "High"), ("Medium", "Medium"), ("Low", "Low"))
STATUS = (("ToDo", "ToDo"), ("InProgress", "InProgress"), ("Done", "Done"))


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=10, choices=TYPE, editable=False)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['author_user_id', 'title'], name='unique_contributor')]
        verbose_name = 'Project'

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=12, choices=PERMISSION, default='Restricted', editable=False)
    role = models.CharField(max_length=12, choices=ROLE, default='Contributor', editable=False)

    class Meta:
        verbose_name = 'Contributor'
        unique_together = ['user_id', 'project_id']

    def __str__(self):
        return f"{self.user_id} - {self.role} - {self.project_id}"


class Issue(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=2500)
    tag = models.CharField(max_length=12, choices=TAG)
    priority = models.CharField(max_length=12, choices=PRIORITY)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=STATUS)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       related_name='author')
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         related_name='assignee')
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['created_time']
        verbose_name = 'Issue'

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=500, blank=False, unique=True)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']
        verbose_name = 'Comment'

    def __str__(self):
        return str(self.description)
