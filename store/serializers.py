from django.db.models import fields
from store.models import Brand, Form, Item, ItemBrand, Product, User
from rest_framework import serializers

# Create Serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'id', 'form_name', 'form_status', 
            'form_instructions', 'available_till'
        ]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id', 'brand_name'
        ]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id', 'item_name',
            'item_description', 'item_category'
        ]
        

class ItemBrandSerializer(serializers.Serializer):
    item = ItemSerializer()
    brand = BrandSerializer()
    quantity_available = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=9, decimal_places=3)

    def create(self, validated_data):
        item_dict = validated_data.pop('item')
        brand_dict = validated_data.pop('brand')
        item = Item.objects.get(**item_dict)
        brand = Brand.objects.get(**brand_dict)
        return ItemBrand.objects.create(
            item=item, brand=brand, **validated_data
        )
    
    def update(self, instance, validated_data):
        instance.quantity_available = validated_data.get_data(
            'quantity_available', instance.quantity_available
        )
        instance.price = validated_data.get_data(
            'price', instance.price
        )
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):

    user = UserSerializer()
    form = FormSerializer()
    item = ItemSerializer()
    brand = BrandSerializer()
    quantity_ordered = serializers.IntegerField()
    quantity_delivered = serializers.IntegerField()

    def create(self, validated_data):
        user_dict = validated_data.pop('user')
        user = User.objects.get(**user_dict)
        form_dict = validated_data.pop('form')
        form = Form.objects.get(**form_dict)
        item_dict = validated_data.pop('item')
        item = Item.objects.get(**item_dict)
        brand_dict = validated_data.pop('brand')
        brand = Brand.objects.get(**brand_dict)
        return Product.objects.create(
            user=user,
            form=form,
            item=item,
            brand=brand,
            **validated_data
        )
    
    def post(self, instance, validated_data):
        instance.quantity_ordered = validated_data.get_data('quantity_ordered', instance.quantity_ordered)
        instance.quantity_delivered = validated_data.get_data('quantity_delivered', instance.quantity_delivered)
        instance.save()
        return instance