from rest_framework import serializers


class CheckCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
