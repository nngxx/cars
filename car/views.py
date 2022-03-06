from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from car.models import Car
from car.serializers import CarSerializer


class CarView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        car_serializer = CarSerializer(cars, many=True)
        return JsonResponse(car_serializer.data, status=status.HTTP_200_OK, safe=False)
