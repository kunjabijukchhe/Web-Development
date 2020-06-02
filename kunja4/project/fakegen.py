import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

import random

from app.models import Record,Website
from faker import Faker

fake=Faker()

def generate(n=5):
    for entry in range(n):

        fake_name=fake.name()
        fake_web=fake.company()
        fake_url=fake.url()

        rec=Record.objects.get_or_create(name=fake_name)[0]
        web=Website.objects.get_or_create(name=rec,webName=fake_web,url=fake_url)[0]


if __name__=='__main__':
    print("Done!")
    generate(24)
    print("Complete!")
