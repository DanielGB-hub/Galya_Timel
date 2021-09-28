from mainapp.models import *
from mainapp.serializers import *
from rest_framework import generics


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PhotoCardListCreate(generics.ListCreateAPIView):
    queryset = PhotoCard.objects.all()
    serializer_class = PhotoCardSerializer


class TextBlockListCreate(generics.ListCreateAPIView):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer


class ImageBlockListCreate(generics.ListCreateAPIView):
    queryset = ImageBlock.objects.all()
    serializer_class = ImageBlockSerializer