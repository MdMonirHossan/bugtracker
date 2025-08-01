from django.db import models

class BaseModel(models.Model):
    """
    @model: BaseModel
    @inherited: models.Model
    @is_abstract: true
    @description: this is the base or parent abstract model for all other models
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(
        default=False,
        help_text='This deleted flag means whether the data is soft deleted or not'
    )

    class Meta:
        abstract = True
