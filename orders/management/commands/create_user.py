from django.core.management.base import BaseCommand
from orders.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Nikita', email='ninkita1992@mail.ru',telephone='898213252525', address='Moscow')
        user.save()
        self.stdout.write(f'{user}')

