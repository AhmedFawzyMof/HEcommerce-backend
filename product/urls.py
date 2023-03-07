from django.urls import path
from product import views

urlpatterns = [
    path('products/<int:product_id>/comments/', views.Comments.as_view({'get': 'list'})),
    path('products/post/comments/', views.PostComments),
    path('latest-products/', views.LatestProductsList.as_view()),
    path('cur-products/', views.CurProductsList.as_view()),
    path('products/search/', views.search),
    path('tags/products/<slug:tag_slug>/', views.TagDetail.as_view()),
    path('allcategoris/', views.AllCategoris.as_view()),
    path('footercategoris/', views.FooterCategoris.as_view()),
    path('allproducts/', views.AllProducts.as_view()),
    path('alltags/',views.AllTags.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/ar/<slug:category_slug>/<slug:product_slug>/', views.ProductArDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
