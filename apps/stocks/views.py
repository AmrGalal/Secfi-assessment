from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework import status

from . import serializers, utils


class VestedEquityValueViewset(GenericViewSet):
    serializer_class = serializers.VestedEquityValueSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = utils.calculate_vested_equity_over_time(request.data)
        return Response(response_data, status=status.HTTP_200_OK)
