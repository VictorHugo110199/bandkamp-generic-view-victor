from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model= Album
        fields = ['id', 'name', 'year', 'user_id']
        # id = serializers.IntegerField(read_only=True)
        # name = serializers.CharField(max_length=255)
        # year = serializers.IntegerField()
        # user_id = serializers.IntegerField(read_only=True)

    # def create(self, validated_data):
    #     return Album.objects.create(**validated_data)
