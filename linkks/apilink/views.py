from rest_framework.viewsets import ModelViewSet
from linkks.models import Link
from linkks.apilink.serializers import LinkSerializer

class LinkViewSet(ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    
    # permission_classes = [IsAuthenticated]  # validacion para que solo gente autenticada pueda ver los links
    
    def get_queryset(self):
        # Filtra los links por el usuario actual
        return Link.objects.all()
