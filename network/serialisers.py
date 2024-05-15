from rest_framework import serializers
from network.models import Provider, Product, Branch


class ProviderSerializer(serializers.ModelSerializer):
    """Сериализатор для поставщика"""

    class Meta:
        model = Provider
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продукта"""

    class Meta:
        model = Product
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    """Сериализатор для ветки сети"""

    level = serializers.SerializerMethodField()

    def get_level(self, obj):
        """Определяет уровень ветки цепи"""
        register_form_seller = obj.seller.register_form

        if register_form_seller == Provider.FormChoice.FACROTY:
            return 1
        else:
            return 2

    class Meta:
        model = Branch
        fields = '__all__'
