from django.shortcuts import render_to_response
from django.template import RequestContext

from lab7.models import HostelModel, RoomModel, StudentModel


# Create your views here.


def get_model(request):
    ID = request.POST.get('ID')
    faculty = request.POST.get('faculty')
    if (ID=='' or ID==None):
        ID="ІС4212"
    if (faculty == '' or faculty == None):
        faculty = "ФІОТ"
    our_student = StudentModel.objects.get(ID=ID)
    hostel=HostelModel.objects.filter(Faculty=faculty)
    return render_to_response('add.html', {'our': our_student,'ID':ID,'hostel':hostel}
                              , RequestContext(request))


def hostel(request):
    Hostel = HostelModel.objects.all()
    return render_to_response('hostel.html', {'Hostel': Hostel}, RequestContext(request))


def room(request):
    Room = RoomModel.objects.all()
    return render_to_response('room.html', {'Room': Room}, RequestContext(request))


def student(request):
    Student = StudentModel.objects.all()
    return render_to_response('student.html', {'Student': Student}, RequestContext(request))
