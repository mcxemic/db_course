from django.contrib import admin
from .models import loopModel,HostelModel,RoomModel,StudentModel
# Register your models here.
admin.site.register(HostelModel)
admin.site.register(StudentModel)
admin.site.register(RoomModel)