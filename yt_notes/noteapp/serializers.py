from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=True)
    body = serializers.CharField(required=True)
    slug = serializers.SlugField(required=False, read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
