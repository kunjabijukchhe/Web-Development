import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","revise.settings")

import django
django.setup()

from reviseApp.models import Record
from faker import Faker
fake=Faker()

def populate(N=10):
    for entry in range(N):
        fake_name=fake.name().split()
        fake_first=fake_name[0]
        fake_last=fake_name[1]
        fake_email=fake.email()

        user=Record.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]
if __name__=='__main__':
    print("Processing...")
    populate()
    print("DONE!")
