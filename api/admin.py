from django.contrib import admin
from .models import School, Course, Teacher, Comment, Registration
from .models import SchoolRu, CourseRu, TeacherRu, CommentRu
from .models import SchoolEn, CourseEn, TeacherEn, CommentEn

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Comment)
admin.site.register(Registration)

# Rus tili vaqtincvhalik
admin.site.register(SchoolRu)
admin.site.register(CourseRu)
admin.site.register(TeacherRu)
admin.site.register(CommentRu)

#Ingliz tili vaqtincvhalik
admin.site.register(SchoolEn)
admin.site.register(CourseEn)
admin.site.register(TeacherEn)
admin.site.register(CommentEn)