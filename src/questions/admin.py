from django.contrib import admin

# Register your models here.
from .models import Question, Result, Title

admin.site.register(Question)
admin.site.register(Title)
admin.site.register(Result)