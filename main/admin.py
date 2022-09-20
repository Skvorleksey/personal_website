from django.contrib import admin
from . import models


# Register your models here.
class WorkExperienceEntryAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'position',
        'start',
        'finish',
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(models.WorkExperienceEntry, WorkExperienceEntryAdmin)
admin.site.register(models.Skill, SkillAdmin)
