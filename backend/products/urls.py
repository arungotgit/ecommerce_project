from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]


from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls