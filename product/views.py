from rest_framework.decorators import api_view
from .models import Product
from django.db.models import Q
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import generics
from .models import *
from .serializers import *
from .pagination import *
from django_filters import rest_framework as filters

class ProductPriceFilter(filters.FilterSet):
    min_price   = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price   = filters.NumberFilter(field_name="price", lookup_expr='lte')
    name        = filters.CharFilter(field_name="name",lookup_expr='icontains')
    nameAr      = filters.CharFilter(field_name="nameAr",lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name','category','nameAr','min_price','max_price']

class Comments(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

    def get_queryset(self):
        return super().get_queryset().filter(product=self.kwargs.get('product_id'))



@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def PostComments(request):
    serializer = PostReviewSerializer(data=request.data)

    if serializer.is_valid():

        try:
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductPriceFilter
    pagination_class = StandardResultsSetPagination


class AllCategoris(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorisSerializer

class FooterCategoris(generics.ListAPIView):
    queryset = Category.objects.all()[0:5]
    serializer_class = CategorisSerializer


class AllTags(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class CurProductsList(generics.ListAPIView):
    queryset = Product.objects.all()[0:3]
    serializer_class = ProductSerializer

class LatestProductsList(generics.ListAPIView):
    queryset = Product.objects.all()[0:8]
    serializer_class = ProductSerializer


class ProductArDetail(APIView):

    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductArSerializer(product)
        return Response(serializer.data)


class ProductDetail(APIView):

    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
                    
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
 
    def get(self, request, category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class TagDetail(APIView):
    def get_object(self, tag_slug):
        try:
            return Tags.objects.get(slug=tag_slug)
        except Tags.DoesNotExist:
            raise Http404
    
 
    def get(self, request, tag_slug):
        tag = self.get_object(tag_slug)
        serializer = TagSerializer(tag)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(nameAr=query) | Q(descriptionAr__icontains=query) )
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"products": []})

