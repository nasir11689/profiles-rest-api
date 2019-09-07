from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('User-profile',views.UserProfileViewSet)
router.register('User-login',views.UserLoginViewSet,base_name='User-login')
router.register('User-Details',views.UserDetailsViewSet)


urlpatterns=[
    url(r'',include(router.urls))
]