from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet, basename='followers')
v1_router.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
