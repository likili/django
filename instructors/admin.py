from django.contrib import admin
from instructors.models import Instructor, Position, Course

admin.site.register(Instructor)
admin.site.register(Position)
admin.site.register(Course)
# Register your models here.
