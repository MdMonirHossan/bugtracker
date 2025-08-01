from django.db import models
from django.contrib.auth.models import User
from libs.core.models.base_models import BaseModel
from libs.utils.constants.model_constants import STATUS_CHOICES, PRIORITY_CHOICES

# Create your models here.

class Project(BaseModel):
    name        = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Project already exists with this name.'})
    description = models.TextField(max_length=1000)
    owner       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    

class Bug(BaseModel):
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status      = models.CharField(choices=STATUS_CHOICES, max_length=20, default='Open')
    priority    = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='Low')
    assigned_to = models.ForeignKey(User, related_name='assigned_bugs', on_delete=models.SET_NULL, null=True)
    project     = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by  = models.ForeignKey(User, related_name='reported_bugs', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    

class Comment(BaseModel):
    bug         = models.ForeignKey(Bug, related_name='comments', on_delete=models.CASCADE)
    commenter   = models.ForeignKey(User, on_delete=models.CASCADE)
    message     = models.TextField(max_length=1000)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Comment by {self.commenter.username} on {self.bug.title}'