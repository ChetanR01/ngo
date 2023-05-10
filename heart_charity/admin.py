from django.contrib import admin
from .models import Volunteer, Contact, Cause, Donate
# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Contact)
admin.site.register(Cause)
admin.site.register(Donate)