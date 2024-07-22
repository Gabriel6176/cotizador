from rest_framework import serializers
from .models import Cliente, Presupuesto, DetallePresupuesto, Ventana, Puerta, Vidrio, Panel, Lama, PVC

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VidrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vidrio
        fields = '__all__'

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = '__all__'

class LamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lama
        fields = '__all__'

class PVCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVC
        fields = '__all__'

class RevestimientoSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if isinstance(instance, Vidrio):
            return VidrioSerializer(instance).data
        elif isinstance(instance, Panel):
            return PanelSerializer(instance).data
        elif isinstance(instance, Lama):
            return LamaSerializer(instance).data
        return super().to_representation(instance)

class VentanaSerializer(serializers.ModelSerializer):
    revestimiento_vidrio = VidrioSerializer()
    revestimiento_panel = PanelSerializer()
    revestimiento_lama = LamaSerializer()

    class Meta:
        model = Ventana
        fields = '__all__'

class PuertaSerializer(serializers.ModelSerializer):
    revestimiento_vidrio = VidrioSerializer()
    revestimiento_panel = PanelSerializer()
    revestimiento_lama = LamaSerializer()

    class Meta:
        model = Puerta
        fields = '__all__'

class ItemSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if isinstance(instance, Ventana):
            return VentanaSerializer(instance).data
        elif isinstance(instance, Puerta):
            return PuertaSerializer(instance).data
        return super().to_representation(instance)

class DetallePresupuestoSerializer(serializers.ModelSerializer):
    ventana = VentanaSerializer()
    puerta = PuertaSerializer()

    class Meta:
        model = DetallePresupuesto
        fields = '__all__'

class PresupuestoSerializer(serializers.ModelSerializer):
    detalles = DetallePresupuestoSerializer(many=True, read_only=True)

    class Meta:
        model = Presupuesto
        fields = '__all__'
