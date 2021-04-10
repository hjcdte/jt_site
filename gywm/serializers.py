from rest_framework import serializers 


class GywmSerializer(serializers.Serializer):
    content = serializers.CharField()
    # content = serializers.CharField()
    img = serializers.CharField()

