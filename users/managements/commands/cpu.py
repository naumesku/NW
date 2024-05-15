from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание super user"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='prp4@bk.ru',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('123qwe')
        user.save()
