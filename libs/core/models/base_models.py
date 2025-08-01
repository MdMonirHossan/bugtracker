from django.db import models

class BaseModel(models.Model):
    """
    @model: BaseModel
    @inherited: models.Model
    @is_abstract: true
    @description: this is the base or parent abstract model for all other models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
