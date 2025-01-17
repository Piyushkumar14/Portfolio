from django.contrib import admin
from .models import Project, Skill, Tag, Message

'''1234, 123456'''

# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)
