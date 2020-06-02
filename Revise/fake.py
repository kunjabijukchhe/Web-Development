import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Revise.settings')

import django
django.setup()

import random
from reviseApp.models import AccessRecord, Webpage, Topic
from faker import Faker

fake=Faker()

topics=['Search','Social','Marketplace','News','Games']
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):


        top=add_topic()
        fake_url=fake.url()
        fake_date=fake.date()
        fake_name=fake.company()
        web=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc=AccessRecord.objects.get_or_create(name=web,date=fake_date)[0]
if __name__=='__main__':
    print("Processing...")
    populate()
    print("DONE!")
