from django.contrib import admin
from .models import (
    Program,
    Session, 
    Semester,
    ProgramType
)
# Register your models here.
admin.site.register(Program)
admin.site.register(ProgramType)
admin.site.register(Session)
admin.site.register(Semester)