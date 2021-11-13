from django.contrib import admin

from backend.views import user
from .models import postedJob, userAppliedJobs, User
# Register your models here.
admin.site.register(postedJob)
admin.site.register(userAppliedJobs)
admin.site.register(User)

