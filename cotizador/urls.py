from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mi_app.views import (
    ClienteViewSet,
    PresupuestoViewSet,
    DetallePresupuestoViewSet,
    VentanaViewSet,
    PuertaViewSet,
    VidrioViewSet,
    PanelViewSet,
    LamaViewSet,
    PVCViewSet
)

# Crear una instancia de DefaultRouter
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'presupuestos', PresupuestoViewSet)
router.register(r'detalles_presupuesto', DetallePresupuestoViewSet)
router.register(r'ventanas', VentanaViewSet)
router.register(r'puertas', PuertaViewSet)
router.register(r'vidrios', VidrioViewSet)
router.register(r'panels', PanelViewSet)
router.register(r'lamas', LamaViewSet)
router.register(r'pvcs', PVCViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Incluye las URLs del router
]

