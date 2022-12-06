from django.contrib import admin

# Register your models here.
from .models import Author,Course

admin.site.register(Author)
admin.site.register(Course)



# # class AdminSchool(admin.ModelAdmin):
# #     list_display=['school_name','city','branch']
# # class AdminStudent(admin.ModelAdmin):
# #     list_display=['name','school','city','branch','fee']


# admin.site.register(School)
# admin.site.register(Student)