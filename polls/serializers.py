from rest_framework import serializers
from .models import Email



class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"


class DummyEmailSerializer(serializers.ModelSerializer):
    from_email = serializers.EmailField(required=False)
    to_email = serializers.EmailField(required=False)
    subject = serializers.CharField(required=False)
    body = serializers.CharField(required=False)

    class Meta:
        model = Email
        fields = "__all__"