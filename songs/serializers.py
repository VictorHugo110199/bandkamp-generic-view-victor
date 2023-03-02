from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    duration = serializers.CharField(max_length=255)
    album_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
