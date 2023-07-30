from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import Response

from .serializers import SensorSerializer, MeasurementSerializer
from .models import Sensor


class SensorsView(ListCreateAPIView):
    def get(self, request) -> Response:
        """ geting sensors list """
        sensors = SensorSerializer(
            Sensor.objects.all(),
            many=True
        )
        return Response(sensors.data)

    def post(self, request) -> Response:
        """ adding new sensor """
        sensor = SensorSerializer(data=request.data)
        if sensor.is_valid():
            sensor.save()
            return Response({'status': 'created'})
        else:
            return Response({'status': 'error'})


class RetvieweSensorView(RetrieveUpdateAPIView):
    def get(self, request, pk: int) -> Response:
        """ geting sensor information """
        sensor = SensorSerializer(
            Sensor.objects.get(id=pk),
            many=False
        )
        return Response(sensor.data)

    def patch(self, request, pk: int) -> Response:
        """ updating sensor information """
        sensor = SensorSerializer(
            Sensor.objects.get(id=pk),
            data=request.data,
            partial=True
        )
        if sensor.is_valid():
            sensor.save()
            return Response({'status': 'updated'})
        else:
            return Response({'status': 'error'})


class CreateMeasurement(CreateAPIView):
    def post(self, request) -> Response:
        """ adding new measurement for sensor """
        measurement = MeasurementSerializer(data=request.data)
        if measurement.is_valid():
            measurement.save()
            return Response({'status': 'created'})
        else:
            return Response({'status': 'error'})
