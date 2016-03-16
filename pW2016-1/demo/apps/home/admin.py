from django.contrib import admin
from .models import Student, Perfil, Professor


@admin.register(Student)
class Student_admin(admin.ModelAdmin):
    list_display = ('student_code', 'student_name', 'student_age', 'student_semester', 'student_career', 'student_image', 'slug')
    list_filter = ('student_code',)
    search_fields = ('student_code', 'student_name',)


@admin.register(Perfil)
class Perfil_admin(admin.ModelAdmin):
    list_display = ('user_perfil', 'mail', 'phone',)
    list_filter = ('mail',)
    search_fields = ('user_perfil', 'mail',)


@admin.register(Professor)
class Profesor_admin(admin.ModelAdmin):
    list_display = ('professor_name', 'class_room', 'get_students',)

    def get_students(self, obj):
    	return "\n".join([p.student_name for p in obj.students.all()])
