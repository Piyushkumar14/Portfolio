from django.contrib import admin
from  .models import Project, Skill, Tag

'''pr141, 1234'''

# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)

