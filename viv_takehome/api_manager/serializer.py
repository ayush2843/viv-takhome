from rest_framework import serializers
from .models import PlaylistData


class PlaylistDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistData
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if "star_rating" in representation and representation["star_rating"] is None:
            del representation["star_rating"]
        return representation
