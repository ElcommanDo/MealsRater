from rest_framework import viewsets
from .serializers import MealSerializer, RatingSerializer
from .models import Meal, Rating
# Create your views here.


class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
