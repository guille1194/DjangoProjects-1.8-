from django.contrib import admin
from .models import Student, Perfil


@admin.register(Student)
class Student_admin(admin.ModelAdmin):
    list_display = ('student_code', 'student_name', 'student_age', 'student_semester', 'student_career', 'student_image',)
    list_filter = ('student_code',)
    search_fields = ('student_code', 'student_name',)


@admin.register(Perfil)
class Student_admin(admin.ModelAdmin):
    list_display = ('user_perfil', 'mail', 'phone',)
    list_filter = ('mail',)
    search_fields = ('user_perfil', 'mail',)
