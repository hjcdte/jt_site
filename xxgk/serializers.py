from rest_framework import serializers


class GgSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    published_time = serializers.DateTimeField()