from django.contrib import admin
from .models import (
    Course,
    StudentCourseRegistration,
    LecturerCourseAssignment,
    CourseDistribution
)

admin.site.register(Course)
admin.site.register(StudentCourseRegistration)
admin.site.register(LecturerCourseAssignment)
admin.site.register(CourseDistribution)
admin.site.title = "Course"