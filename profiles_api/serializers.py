from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for tetingour APIView"""
    name = serializers.CharField(max_length=10)
