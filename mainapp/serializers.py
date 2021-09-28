from rest_framework import serializers
from mainapp.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'slug')


class PhotoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCard
        fields = ('title', 'photo', 'publication_date', 'category')


class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = ('title', 'information')


class ImageBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBlock
        fields = ('title', 'image')



