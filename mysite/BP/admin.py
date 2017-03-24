from django.contrib import admin

# Register your models here.

from .models import Posting, Founder

admin.site.register(Posting)
admin.site.register(Founder)
