from rest_framework import serializers
from .models import Project, Bug, Comment

class ProjectSerializer(serializers.ModelSerializer):
    """
    This serializer is responsible for serializing and deserializing of Project models instance.
    model: Project
    fields: __all__
    """
    class Meta:
        model   = Project
        fields  = '__all__'


class BugSerializer(serializers.ModelSerializer):
    """ 
    This serializer is responsible for serializing and deserializing of Bug models instance.
    model: Bug
    fields: __all__
    """
    class Meta:
        model   = Bug
        fields  = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    This serializer is responsible for serializing and deserializing of Comment models instance.
    model: Comment
    fields: __all__
    """
    class Meta:
        model   = Comment
        fields  = '__all__'