from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet, 
    BugViewSet, 
    CommentViewSet, 
    BugAssignedApiView, 
    BugFilterApiView
)

# custom urls for APIView
custom_urls = [
    path('bugs/assigned', BugAssignedApiView.as_view(), name='bug_assigned'),
    path('bugs/filter', BugFilterApiView.as_view(), name='bug_filter')
]

# Default router initialization
router = DefaultRouter(trailing_slash=False)

# Register route for ViewSets
router.register(r'projects/?', ProjectViewSet, basename='project_viewset')
router.register(r'bugs/?', BugViewSet, basename='bug_viewset')
router.register(r'comments/?', CommentViewSet, basename='comment_viewset')

# Urls for tracker app
urlpatterns = custom_urls + router.urls


