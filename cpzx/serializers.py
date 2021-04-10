from rest_framework import serializers 


class CP_IndexSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cp_name = serializers.CharField()
    cp_type__cp_type = serializers.CharField()
    # content = serializers.CharField()
    img = serializers.CharField()


class CP_Type_ListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cp_type = serializers.CharField()
    content = serializers.CharField()
    # content = serializers.CharField()
    img = serializers.CharField()

class CP_Type_DetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cp_type = serializers.CharField()
    cp_name = serializers.CharField()
    # content = serializers.CharField()
    img = serializers.CharField()
    
    class Meta:
        depth = 1