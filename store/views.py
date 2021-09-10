from django.db.models.fields import BigIntegerField
from store.serializers import BrandSerializer, FormSerializer, ItemBrandSerializer, ItemSerializer, UserSerializer
from store.models import Brand, Item, ItemBrand, User, Form
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

def index(request):
    return HttpResponse("Hello World")



class UserList(APIView):
    """
    List all users, or create a new snippet.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormList(APIView):
    """
    List all forms, or create a new snippet.
    """
    def get(self, request, format=None):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemList(APIView):
    """
    List all forms, or create a new snippet.
    """
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BrandList(APIView):
    """
    List all forms, or create a new snippet.
    """
    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemBrandList(APIView):
    """
    List all forms, or create a new snippet.
    """
    def get(self, request, format=None):
        itembrands = ItemBrand.objects.all()
        serializer = FormSerializer(itembrands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        item_id = request.data['item']
        brand_id = request.data['brand']
        item = Item.objects.get(pk=item_id)
        brand = Brand.objects.get(pk=brand_id)
        item_serializer = ItemSerializer(item)
        brand_serializer = BrandSerializer(brand)
        request.data['item'] = item_serializer.data
        request.data['brand'] = brand_serializer.data
        serializer = ItemBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
