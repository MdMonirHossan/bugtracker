from rest_framework.routers import DefaultRouter
from .views import (
    ActivityLogViewSet
)

# Default router initialization
router = DefaultRouter(trailing_slash=False)

# Register route for ViewSets
router.register(r'activity-logs/?', ActivityLogViewSet, basename='activity_logs_viewset')


urlpatterns = router.urls