from django.contrib import admin
from member.models import Member

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=('id','nickname','status','age','created_at',)
    ordering=['id']