from rest_framework import serializers
from .models import ActivityLog


class ActivityLogSerializer(serializers.ModelSerializer):
    """
    This serializer is responsible for serializing and deserializing of Activity models instance.
    model: ActivityLog
    fields: __all__
    """
    class Meta:
        model = ActivityLog
        fields = '__all__'