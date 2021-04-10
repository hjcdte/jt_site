from rest_framework import serializers


class Jj_IndexSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    published_time = serializers.DateTimeField()


class Img_IndexSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    img = serializers.CharField()