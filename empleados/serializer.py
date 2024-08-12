from rest_framework import serializers
from empleados.models import Departamento, Empleado

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamento
        fields= '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields= '__all__'