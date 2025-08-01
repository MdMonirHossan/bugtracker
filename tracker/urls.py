from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet, 
    BugViewSet, 
    CommentViewSet, 
    BugAssignedApiView, 
    BugFilterApiView
)

# Default router initialization
router = DefaultRouter()

# Register route for ViewSets
router.register('projects', ProjectViewSet)
router.register('bugs', BugViewSet)
router.register('comments', CommentViewSet)

# custom urls for APIView
custom_urls = [
    path('bugs/assigned', BugAssignedApiView.as_view(), name='bug_assigned'),
    path('bugs/filter', BugFilterApiView.as_view(), name='bug_filter')
]

# Urls for tracker app
urlpatterns = router.urls + custom_urls



