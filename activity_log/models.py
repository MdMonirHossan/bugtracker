from django.db import models
from django.contrib.auth.models import User
from tracker.models import Project
from libs.core.models.base_models import BaseModel
from libs.utils.constants.model_constants import ACTION_CHOICES


# Create your models here.

class ActivityLog(BaseModel):
    """
    Model to store various activity logs within the application.
    """
    project     = models.ForeignKey(
                        Project, 
                        on_delete=models.CASCADE, 
                        related_name='activity_logs', 
                        help_text='Activity under which project.'
                )
    user        = models.ForeignKey(
                        User, 
                        on_delete=models.SET_NULL, 
                        null=True, 
                        related_name='activity_logs', 
                        help_text='The user who performed the action'
                )
    action      = models.CharField(max_length=100)
    description = models.TextField()
    data        = models.TextField(null=True)
    ip_address  = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Activity Logs'
        ordering = ('-created_at',)

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.action} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            return f"{self.action} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

