from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(AboutSection)
admin.site.register(Skill)
admin.site.register(education)
admin.site.register(Experience)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(SocialLink)
admin.site.register(Contact)