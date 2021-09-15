from django.db.models.fields import BigIntegerField
from store.serializers import BrandSerializer, FormSerializer, ItemBrandSerializer, ItemSerializer, ProductSerializer, UserSerializer
from store.models import Brand, Item, ItemBrand, Product, User, Form
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

def index(request):
    return HttpResponse("Hello World")



class UserList(APIView):
    """
    List all users, or create a new user.
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

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FormList(APIView):
    """
    List all forms, or create a new user.
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

class FormDetail(APIView):
    """
    Retrieve, update or delete a form instance.
    """
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        form = self.get_object(pk)
        serializer = FormSerializer(form)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        form = self.get_object(pk)
        serializer = FormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        form = self.get_object(pk)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemList(APIView):
    """
    List all Items, or create a new Item.
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

class ItemDetail(APIView):
    
    """
    Retrieve, update or delete a item instance.
    """

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandList(APIView):
    """
    List all Brands, or create a new brand.
    """
    def get(self, request, format=None):
        try:
            brands = Brand.objects.all()
        except Brand.DoesNotExist:
            raise Http404
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BrandDetail(APIView):
    
    """
    Retrieve, update or delete a brand instance.
    """

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemBrandList(APIView):
    """
    List all ItemBrand, or create a new itembrand.
    """
    def get(self, request, format=None):
        try:
            itembrands = ItemBrand.objects.all()
        except ItemBrand.DoesNotExist:
            raise Http404
        serializer = ItemBrandSerializer(itembrands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # get ids
        item_id = request.data['item']
        brand_id = request.data['brand']
        # get objects
        item = Item.objects.get(pk=item_id)
        brand = Brand.objects.get(pk=brand_id)
        # create serializer objects
        item_serializer = ItemSerializer(item)
        brand_serializer = BrandSerializer(brand)
        # update request
        request.data['item'] = item_serializer.data
        request.data['brand'] = brand_serializer.data

        serializer = ItemBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):

    """
    List all products or create a new product instance
    """

    def get(self, request, format=None):
        try:
            products = Product.objects.all()
        except Product.DoesNotExist:
            raise Http404
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        # id, object, respective serializer 
        user_id = request.data['user']
        user = User.objects.get(pk=user_id)
        userserializer = UserSerializer(user)

        form_id = request.data['form']
        form = Form.objects.get(pk=form_id)
        formserializer = FormSerializer(form)

        item_id = request.data['item']
        item = Item.objects.get(pk=item_id)
        itemserializer = ItemSerializer(item)

        brand_id = request.data['brand']
        brand = Brand.objects.get(pk=brand_id)
        brandserializer = BrandSerializer(brand)

        # update request
        request.data['user'] = userserializer.data
        request.data['form'] = formserializer.data
        request.data['item'] = itemserializer.data
        request.data['brand'] = brandserializer.data

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

