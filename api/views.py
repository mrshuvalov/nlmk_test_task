from rest_framework import viewsets, status
from api.models import Table
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializers import TableSerializer
from datetime import date, timedelta


class TableViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    @action(
        methods=['get'], name='get_table', detail=False,
    )
    def get_table(self, request):
        table = Table.objects.all()
        res = TableSerializer(table, many=True).data
        return Response(res)

    @action(
        methods=['post'], name='edit_table', detail=False,
    )
    def edit_table(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            tab_row = Table.objects.filter(x_axis=data['x_axis'], y_axis=data['y_axis'])
            if len(tab_row) > 0:
                row  = tab_row.first()
                row.value = data['value']
                row.save()
            else:
                new_tab_row = Table(x_axis=data['x_axis'], y_axis=data['y_axis'], value=data['value'])
                new_tab_row.save()
            return Response(status=status.HTTP_200_OK)
