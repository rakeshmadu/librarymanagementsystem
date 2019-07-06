from django.contrib import admin

# Register your models here.
from .models import bookdata,studentdata


class DataAdmin(admin.ModelAdmin):
    list_display=['book_id','Book_name','Author_name']

admin.site.register(bookdata,DataAdmin)


# class studentadmin(admin.ModelAdmin):
#     list_display = ['Student_name','Branch']

# admin.site.register(studentdata,studentadmin)
