from django.conf import settings
from django.urls import include, path

from accounts import admin
from core.settings import STATIC_URL
from .views import MyProfileView, UserProfileDetailView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('me/', MyProfileView.as_view(), name='my-profile'),
    path('user/<str:user__username>/', UserProfileDetailView.as_view(), name='user-profile'),
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow-user'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/accounts/', include('accounts.urls')),
] + STATIC_URL(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
