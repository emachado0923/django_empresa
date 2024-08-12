from rest_framework import viewsets
from empleados.models import Departamento,Empleado
from empleados.serializer import EmpleadoSerializer,DepartamentoSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all()
    serializer_class=EmpleadoSerializer