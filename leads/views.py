from rest_framework import generics

from leads.models import Lead
from leads.serializers import LeadSerializer

# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
