from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель', **NULLABLE)
    date_release = models.DateField(auto_now_add=True, verbose_name='Дата выхода продукта', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Provider(models.Model):
    """Модель поставщика"""

    class FormChoice(models.TextChoices):
        FACROTY = 'factory', 'завод'
        IP = 'ip', 'индивидуальный предприниматель'
        RS = 'rs', 'розничеая сеть'

    register_form = models.CharField(choices=FormChoice.choices, verbose_name='форма регистрации')
    name = models.CharField(max_length=150, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='старна', **NULLABLE)
    town = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='номер дома', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Branch(models.Model):
    """Модель ветки сети"""
    name = models.CharField(max_length=150, verbose_name='название')
    buyer = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='buyers')
    seller = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='sellers')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолжность')
    time = models.DateTimeField(auto_now=True, verbose_name='время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ветка сети"
        verbose_name_plural = "Ветки сети"
