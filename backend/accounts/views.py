from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile
from .serializers import UserProfileSerializer

class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'user__username'

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            target_user = User.objects.get(username=username)
            if target_user == request.user:
                return Response({'error': 'Você não pode seguir a si mesmo.'}, status=400)
            request.user.profile.following.add(target_user.profile)
            return Response({'status': f'Você agora segue {username}.'})
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=404)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            target_user = User.objects.get(username=username)
            request.user.profile.following.remove(target_user.profile)
            return Response({'status': f'Você deixou de seguir {username}.'})
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=404)
