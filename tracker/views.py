from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .models import Project, Bug, Comment
from .serializers import ProjectSerializer, BugSerializer, CommentSerializer
from rest_framework.response import Response

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewSet will provide API endpoints that allows authenticated users to perform CRUD operations on Project.
    
    Permissions:
    - Only authenticated users can access this endpoints.

    Supported Methods & Endpoints:
    - GET     /api/projects         -> List all Projects
    - GET     /api/projects/{id}    -> Retrieve a specific Project
    - POST    /api/projects         -> Create a new Project
    - PUT     /api/projects/{id}    -> Update an existing Project 
    - PATCH   /api/projects/{id}    -> Partially update a Project
    - DELETE  /api/projects/{id}    -> Delete a Project
    """
    queryset            = Project.objects.all()
    serializer_class    = ProjectSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BugViewSet(viewsets.ModelViewSet):
    """
    This viewSet will provide API endpoints that allows authenticated users to perform CRUD operations on Bug.
    
    Permissions:
    - Only authenticated users can access this endpoints.

    Supported Methods & Endpoints:
    - GET     /api/bugs         -> List all Bugs
    - GET     /api/bugs/{id}    -> Retrieve a specific Bug
    - POST    /api/bugs         -> Create a new Bug
    - PUT     /api/bugs/{id}    -> Update an existing Bug 
    - PATCH   /api/bugs/{id}    -> Partially update a Bug
    - DELETE  /api/bugs/{id}    -> Delete a Bug
    """
    queryset            = Bug.objects.all()
    serializer_class    = BugSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewSet will provide API endpoints that allows authenticated users to perform CRUD operations on Comment.
    
    Permissions:
    - Only authenticated users can access this endpoints.

    Supported Methods & Endpoints:
    - GET     /api/comments         -> List all Comments
    - GET     /api/comments/{id}    -> Retrieve a specific Comment
    - POST    /api/comments         -> Create a new Comment
    - PUT     /api/comments/{id}    -> Update an existing Comment 
    - PATCH   /api/comments/{id}    -> Partially update a Comment
    - DELETE  /api/comments/{id}    -> Delete a Comment
    """
    queryset            = Comment.objects.all()
    serializer_class    = CommentSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)


class BugAssignedApiView(APIView):
    """
    This APIView provide API endpoint to retrieve bugs assigned to the currently authenticate user.

    Permissions:
    - Only authenticated user can access this endpoint

    Method & Endpoint:
    - GET   /api/bugs/assigned  -> Returns a list of bugs where the authenticated user is assigned.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        bugs = Bug.objects.filter(assigned_to=request.user)
        serializer = BugSerializer(bugs, many=True)
        return Response(serializer.data)
    

class BugFilterApiView(APIView):
    """
    This APIView provide API endpoint to retrieve bugs based on status or/and project.

    Permissions:
    - Only authenticated users can access this endpoint

    Method & Endpoint:
    - GET   /api/bugs/filter?status=open&project=1   -> Returns a list of bugs based on status or/and project.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        status  = request.query_params.get('status')
        project = request.query_params.get('project')

        bugs = Bug.objects.all()

        if status:
            bugs = bugs.filter(status__iexact=status)   # filter by exact match

        if project:
            try:
                bugs = bugs.filter(project_id=int(project))
            except ValueError:
                return Response({'error': 'Project ID must be an integer'}, status=400)
            
        serializer = BugSerializer(bugs, many=True)
        return Response(serializer.data)
