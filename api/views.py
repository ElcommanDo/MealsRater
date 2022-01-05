from rest_framework import viewsets, status
from .serializers import MealSerializer, RatingSerializer, UserSerializer
from .models import Meal, Rating, User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
# Create your views here.


class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]

    @action(methods=['POST', ], detail=True)
    def create_rate(self, request, pk):
        if 'stars' in request.data:
            meal = Meal.objects.get(pk=pk)
            user = request.user
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
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def update(self, request, *args, **kwargs):
        response = {'message':
                    'this is not the right way to make update',
                    'status': status.HTTP_400_BAD_REQUEST
                    }
        return Response(response)

    def create(self, request, *args, **kwargs):
        response = {'message':
                    'this is not the right way to make create',
                    'status': status.HTTP_400_BAD_REQUEST
                    }
        return Response(response)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            token, created = Token.objects.get_or_create(user=serializer.instance)
            response = {'token': token.key, }
            return Response(response)
        else:
            response = {'message': 'something went wrong'}
            return Response(response)

