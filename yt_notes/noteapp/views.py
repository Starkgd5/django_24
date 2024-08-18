from django.db.models import Q
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .serializers import NoteSerializer


class NoteListCreateAPIView(ListCreateAPIView):
    queryset = Note.objects.all().order_by('created')
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.filter()
    serializer_class = NoteSerializer
    lookup_field = 'slug'


class SearchNotesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get("search")
        notes = Note.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(category__icontains=query)
        )
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
