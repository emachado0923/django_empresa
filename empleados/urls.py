from rest_framework.routers import DefaultRouter
from empleados.views import DepartamentoViewSet,EmpleadoViewSet

router=DefaultRouter()
router.register('departamento',DepartamentoViewSet,basename='departamento')
router.register('empleado',EmpleadoViewSet,basename='empleado')

urlpatterns=router.urls