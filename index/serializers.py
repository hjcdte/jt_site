from rest_framework import serializers


class Syimg_IndexSerializer(serializers.Serializer):
    img = serializers.CharField()
