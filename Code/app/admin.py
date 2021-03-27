from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Student


# @admin.register(Student)
# class PersonAdmin(ImportExportModelAdmin):
#     list_display = ("name",
#                     "number",
#                     "email",
#                     "linkedin",
#                     "github",
#                     "gender",
#                     "education_level",
#                     "it_background",
#                     "address")
