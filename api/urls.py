from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealView, RatingView
router = DefaultRouter()
router.register('meals', MealView)
router.register('ratings', RatingView)

urlpatterns = [
    path('', include(router.urls)),
]
