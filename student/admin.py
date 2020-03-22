from django.contrib import admin

from .models import Student, Reword
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'sex','major', 'studentID', 'email', 'qq', 'phone','status', 'create_time')
	list_filter = ('sex', 'status','create_time','major')
	search_fields = ('name', 'studentID')
	fieldsets=(
	(None, {
	'fields':(
	('name','major'),
	('sex','studentID'),
	('email','qq','phone'),
	'status',
	)
	}),
    )
    
#@admin.register(Reword)
#class TagAdmin(admin.ModelAdmin):
    #list_display = ('name','status','created_time','intro')
    #fields = ('name','status','intro')
    
    #def save_model(self, request, obj, form, change):
        #obj.owner = request.user
        #return super(TagAdmin, self).save_model(request, obj, form, change)