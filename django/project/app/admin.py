from django.contrib import admin
from app.models import AccessRecord,Topic,Webpage
from app.models1 import User
# Register your models here.

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(User)
