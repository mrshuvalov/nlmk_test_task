from rest_framework import serializers
from api.models import Table


class TableSerializer(serializers.ModelSerializer):
    x_axis = serializers.IntegerField()
    y_axis = serializers.IntegerField()
    value = serializers.CharField()

    class Meta:
        model = Table
        fields = '__all__'
