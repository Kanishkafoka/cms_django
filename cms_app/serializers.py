from rest_framework import serializers
from .models import Admin, Author

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '_all_'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '_all_'
        