from rest_framework import viewsets
from .serializers import MealSerializer, RatingSerializer
from .models import Meal, Rating, User
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['POST', ], detail=True)
    def create_rate(self, request, pk):
        if 'stars' in request.data:
            meal = Meal.objects.get(pk=pk)
            username = request.data['username']
            user = User.objects.get(username=username)
            stars = request.data['stars']

            try:
                # update
                obj = Rating.objects.get(meal=meal, user=user)
                print(obj)
                obj.stars = stars
                obj.save()
                serializer = RatingSerializer(obj, many=False)
                response = {
                    'message': 'Rating is updated',
                    'result': serializer.data
                }
                return Response(response)

            except:
                rate = Rating(meal=meal, user=user, stars=stars)
                rate.save()
                serializer = RatingSerializer(rate, many=False)
                response = {'message': 'Rating is created',
                            'result': serializer.data
                            }
                return Response(response)
        else:
            response = {'message': 'error stars not provided'}
            return Response(response)


class RatingView(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
