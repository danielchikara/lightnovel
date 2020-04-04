from apps.index.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet, base_name='users')