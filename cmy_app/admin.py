from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
class MyuserAdmin(admin.ModelAdmin):

    fieldsets = (('Standard Info', {
        "fields":("full_name","first_name","last_name",'dob','email','phone_number','compy','is_ceo',"password"  )
        }),
        ('Address Info ', {
            'fields':('address','state')
        }),)
    list_display = ('full_name', 'compy', 'email', "created_at","updated_at", "deleted_at",'status')
    def status(self,obj):
        try:
            if obj.is_ceo == True:
                return "CEO"
            return "employee"
        except:
            return None


admin.site.register(Myuser , MyuserAdmin)
admin.site.register(Company)


