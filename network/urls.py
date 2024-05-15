from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.apps import NetworkConfig
from network.views import *

app_name = NetworkConfig.name

router_branch = DefaultRouter()
router_branch.register(r'branch', BranchViewSet, basename='branch')

router_provider = DefaultRouter()
router_provider.register(r'provider', ProviderViewSet, basename='provider')

router_product = DefaultRouter()
router_product.register(r'product', ProductViewSet, basename='product')

# urlpatterns = [
#     path('', include(router_branch.urls)),
#     path('', include(router_provider.urls)),
#     path('', include(router_product.urls)),
# ]

urlpatterns = [] + router_branch.urls + router_provider.urls + router_product.urls
