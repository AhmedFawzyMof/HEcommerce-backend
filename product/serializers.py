from rest_framework import serializers
from .models import *

class ProductArSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        queryset = Tags.objects.all(),
        slug_field='name',
    )

    sizes = serializers.SlugRelatedField(
        many=True,
        queryset = Size.objects.all(),
        slug_field='name',
    )

    colors = serializers.SlugRelatedField(
        many=True,
        queryset = Color.objects.all(),
        slug_field='name',
    )


    class Meta:
        model = Product
        fields = (
            "id",
            "sizes",
            "colors",
            "name",
            "nameAr",
            "tag",
            "category",
            "get_absolute_url",
            "description",
            "descriptionAr",
            "price",
            'image',
        )



class ProductSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        queryset = Tags.objects.all(),
        slug_field='name',
    )

    sizes = serializers.SlugRelatedField(
        many=True,
        queryset = Size.objects.all(),
        slug_field='name',
    )

    colors = serializers.SlugRelatedField(
        many=True,
        queryset = Color.objects.all(),
        slug_field='name',
    )


    class Meta:
        model = Product
        fields = (
            "id",
            "sizes",
            "colors",
            "name",
            "nameAr",
            "tag",
            "category",
            "get_absolute_url",
            "description",
            "descriptionAr",
            "price",
            'image',
        )

class TagSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Tags 
        fields = (
            "id",
            "nameAr",
            "slug",
            "products"
        )

class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags 
        fields = (
            "id",
            "get_absolute_url",
            "name",
            "nameAr",
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "nameAr",
            "products",
        )

class CategorisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "nameAr",
            "name",
            "get_absolute_url",
        )

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "get_username",
            "product",
            "titles",
            "rate",
            "react",
            "comment",
            'get_email',
        )

class PostReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "product",
            "titles",
            "rate",
            "react",
            "comment",
        )
