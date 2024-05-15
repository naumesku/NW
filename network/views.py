from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from network.models import Provider, Product, Branch
from network.serialisers import ProviderSerializer, ProductSerializer, BranchSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """Представление поставщика"""
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """Представление Продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BranchViewSet(viewsets.ModelViewSet):
    """Представление Ветки сети"""
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    filter_backends = [SearchFilter]
    filterset_fields = ['country']


    def update(self, request, *args, **kwargs):
        """Функция запрещает обновлять задолжность"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if partial and 'debt' in request.data:
            request.data.pop('debt')

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
