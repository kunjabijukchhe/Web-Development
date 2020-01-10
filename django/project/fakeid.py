import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()



import random

from app.models import Topic,Webpage,AccessRecord

from faker import Faker

fake=Faker()

topics=['Search','Socail Networking','News','Games','Marketpalce']


def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top=add_topic()

        #fake date entry
        fake_url=fake.url()
        fake_date=fake.date()
        fake_name=fake.company()


        web=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        access=AccessRecord.objects.get_or_create(name=web,date=fake_date)[0]

if __name__=='__main__':
    print("populate script!")
    populate(20)
    print("populating complete!")
