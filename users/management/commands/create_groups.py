from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Кастомная команда для создания группы пользователей"""

    def handle(self, *args, **options):
        group_name = options["group_name"]

        if Group.objects.filter(name=group_name).exists():
            self.stdout.write(
                self.style.WARNING(f'Группа с именем "{group_name}" уже существует')
            )
        else:
            group = Group(name=group_name)
            group.save()
            self.stdout.write(
                self.style.SUCCESS(f'Группа "{group_name}" была успешно создана')
            )
