from django.core.management.base import BaseCommand
from users.models import CustomsUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = CustomsUser.objects.create(
            email='test@mail.ru',
            first_name='admin',
            last_name='admin'
        )

        user.set_password('1234')

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user with email {user.email}!'))
