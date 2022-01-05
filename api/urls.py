from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealView, RatingView, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('meals', MealView)
router.register('ratings', RatingView)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
]
