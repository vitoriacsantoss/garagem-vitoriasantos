from rest_framework.serializers import ModelSerializer
from core.models import Acessorio
class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
        max_length = 100