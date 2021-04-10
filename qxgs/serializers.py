from rest_framework import serializers


class Qxgs_ListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    qxgs_name = serializers.CharField()
    simple_content = serializers.CharField()
    img = serializers.CharField()


class Qxgs_DetailSerializer(serializers.Serializer):
    qxgs_name = serializers.CharField()
    content = serializers.CharField()
    img = serializers.CharField()