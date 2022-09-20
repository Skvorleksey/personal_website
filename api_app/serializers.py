from rest_framework import serializers
from users.models import User
from blog.models import BlogPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'company', 'hobby',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    edited = serializers.ReadOnlyField()
    publication_date_time = serializers.ReadOnlyField()

    class Meta:
        model = BlogPost
        fields = '__all__'


class CreateUpdatePostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = BlogPost
        fields = ('author', 'text',)
