from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, Presupuesto, DetallePresupuesto, Ventana, Puerta, Vidrio, Panel, Lama, PVC
from .serializers import (
    ClienteSerializer,
    PresupuestoSerializer,
    DetallePresupuestoSerializer,
    VentanaSerializer,
    PuertaSerializer,
    VidrioSerializer,
    PanelSerializer,
    LamaSerializer,
    PVCSerializer
)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer

    def create(self, request, *args, **kwargs):
        cliente_data = request.data.get('cliente')
        if cliente_data:
            cliente, created = Cliente.objects.get_or_create(email=cliente_data['email'], defaults=cliente_data)
        else:
            return Response({"error": "Cliente no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

        numero = Presupuesto.objects.count() + 1
        presupuesto = Presupuesto.objects.create(cliente=cliente, numero=numero, **request.data)
        serializer = self.get_serializer(presupuesto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def agregar_item(self, request, pk=None):
        presupuesto = self.get_object()
        detalle_data = request.data
        item_data = detalle_data.pop('item', None)

        if item_data:
            if 'revestimiento_vidrio' in item_data:
                revestimiento_data = item_data.pop('revestimiento_vidrio', None)
                if revestimiento_data:
                    revestimiento, created = Vidrio.objects.get_or_create(**revestimiento_data)
                    item_data['revestimiento_vidrio'] = revestimiento.id

            elif 'revestimiento_panel' in item_data:
                revestimiento_data = item_data.pop('revestimiento_panel', None)
                if revestimiento_data:
                    revestimiento, created = Panel.objects.get_or_create(**revestimiento_data)
                    item_data['revestimiento_panel'] = revestimiento.id

            elif 'revestimiento_lama' in item_data:
                revestimiento_data = item_data.pop('revestimiento_lama', None)
                if revestimiento_data:
                    revestimiento, created = Lama.objects.get_or_create(**revestimiento_data)
                    item_data['revestimiento_lama'] = revestimiento.id

            if 'ventana' in item_data:
                item = Ventana.objects.create(**item_data)
            elif 'puerta' in item_data:
                item = Puerta.objects.create(**item_data)
            else:
                return Response({"error": "Tipo de item no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Item no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

        detalle_data['ventana'] = item.id if 'ventana' in item_data else None
        detalle_data['puerta'] = item.id if 'puerta' in item_data else None
        detalle_data['presupuesto'] = presupuesto.id
        detalle_serializer = DetallePresupuestoSerializer(data=detalle_data)

        if detalle_serializer.is_valid():
            detalle_serializer.save()
            return Response(detalle_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VentanaViewSet(viewsets.ModelViewSet):
    queryset = Ventana.objects.all()
    serializer_class = VentanaSerializer

class PuertaViewSet(viewsets.ModelViewSet):
    queryset = Puerta.objects.all()
    serializer_class = PuertaSerializer

class VidrioViewSet(viewsets.ModelViewSet):
    queryset = Vidrio.objects.all()
    serializer_class = VidrioSerializer

class PanelViewSet(viewsets.ModelViewSet):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer

class LamaViewSet(viewsets.ModelViewSet):
    queryset = Lama.objects.all()
    serializer_class = LamaSerializer

class PVCViewSet(viewsets.ModelViewSet):
    queryset = PVC.objects.all()
    serializer_class = PVCSerializer

class DetallePresupuestoViewSet(viewsets.ModelViewSet):
    queryset = DetallePresupuesto.objects.all()
    serializer_class = DetallePresupuestoSerializer

        
