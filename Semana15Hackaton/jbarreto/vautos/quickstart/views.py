from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from vautos.quickstart.serializers import UserSerializer, GroupSerializer
#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    
    # def get_queryset(self):
    #     queryset = User.objects.all().order_by('-date_joined')
    #     username = self.request.query_params.get('username',None)
    #     if username is not None:
    #         queryset = queryset.filter(username= username)
    #     return queryset
    


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    