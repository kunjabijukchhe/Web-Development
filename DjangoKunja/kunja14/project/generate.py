import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()


from app.models import User
from faker import Faker

fake=Faker('ne_NP')

def generate(n=5):
    for entry in range(n):
        fake_name=fake.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[-1]
        fake_email=fake.email()

        user=User.objects.get_or_create(First_name=fake_first_name,Last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("Going...")
    generate(20)
    print("DONE!")
