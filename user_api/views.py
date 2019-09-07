from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from . import permissions


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserLogin.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateUserProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    def create(self,request):
        return ObtainAuthToken().post(request)




class UserDetailsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserDetailsSerailizer
    permission_classes = (permissions.PostOwnUserDetails, IsAuthenticated)
    queryset = models.UserDetails.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)