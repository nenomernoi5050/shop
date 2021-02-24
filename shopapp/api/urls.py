from django.urls import path

from rest_framework import routers
from .views import *


router = routers.SimpleRouter()

router.register('sub-category', SubCategoryViewSet, basename='Разделы')
router.register('category', CategoryViewSet, basename='Категории')
router.register('product', ProductViewSet, basename='Товары')

urlpatterns = []
urlpatterns +=router.urls