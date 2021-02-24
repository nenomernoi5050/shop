from rest_framework import viewsets
from .serialayzers import *
from parser_site.models import *


class SubCategoryViewSet(viewsets.ModelViewSet):

    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer


    action_to_serializer = {
        "retrieve": ProductSubCategorySerializer
    }


    def get_serializer_class(self, *args, **kwargs):

        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )



class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = CardProduct.objects.all()
    serializer_class = ProductSerializer



    action_to_serializer = {
        "list": ProductListRetrieveSerializer,
        "retrieve": ProductListRetrieveSerializer
    }


    def get_serializer_class(self, *args, **kwargs):

        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )

