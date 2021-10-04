from django.contrib import admin
from report.models import Report, Category, Verdict

admin.site.register(Report)
admin.site.register(Category)
admin.site.register(Verdict)
