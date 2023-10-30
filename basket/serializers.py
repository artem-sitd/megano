import pytz
from django.core.validators import MaxValueValidator
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response
from tags.models import Tags
from .models import Basket
from product.models import Product, Reviews, ProductImage


# для ProductSerializer
class ReviewsSerializer(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, instance):
        len_review = Reviews.objects.filter(product=instance.id)
        return len(len_review)


# для ProductSerializer
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('src', 'alt')


# для ProductSerializer
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name')


# для BasketSerializer*******************************************************************************
class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=8, decimal_places=2, coerce_to_string=False)
    reviews = ReviewsSerializer()
    images = ImagesSerializer(many=True)
    tags = TagsSerializer(many=True)
    rating = serializers.DecimalField(max_digits=2, decimal_places=1, default=3.0,
                                      validators=[MaxValueValidator(5.0)], coerce_to_string=False)
    date = SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'price', 'count', 'date', 'title', 'description', 'free_delivery',
                  'images', 'tags', 'reviews', 'rating')

    def get_date(self, obj):
        temp = obj.date.astimezone(pytz.timezone('CET'))
        return temp.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0100 (Central European Standard Time)'


# api/Basket
class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Basket
        fields = ['product']


class BasketSerializer2(serializers.Serializer):
    # price = serializers.DecimalField(max_digits=8, decimal_places=2, coerce_to_string=False)
    # reviews = ReviewsSerializer()
    # images = ImagesSerializer(many=True)
    # tags = TagsSerializer(many=True)
    # rating = serializers.DecimalField(max_digits=2, decimal_places=1, default=3.0,
    #                                   validators=[MaxValueValidator(5.0)], coerce_to_string=False)
    date = SerializerMethodField()

    def get_date(self, obj):
        temp = obj.date.astimezone(pytz.timezone('CET'))
        return temp.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0100 (Central European Standard Time)'

    def to_representation(self, instance):
        image = ProductImage.objects.get(product=instance.id)
        len_review = Reviews.objects.filter(product=instance.id)
        tags = instance.tags.all()
        list_product = [{'id': instance.id, 'category': instance.category.id,
                         'price': instance.price, 'count': instance.count,
                         'date': instance.date.strftime(
                             '%a %b %d %Y %H:%M:%S') + ' GMT+0100 (Central European Standard Time)',
                         'title': instance.title, 'description': instance.description,
                         'free_delivery': instance.free_delivery,
                         'images': [{'src': image.src.url, 'alt': image.alt}],
                         'tags': [{'id': j.id, 'name': j.name} for j in tags],
                         'reviews': len(len_review),
                         'rating': instance.rating},
                        ]
        return list_product
