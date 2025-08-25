from rest_framework import serializers
from linkks.models import Link
from users.models import User

class LinkSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Link
        fields = '__all__'