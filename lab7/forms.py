from django import forms


class LoopForm(forms.Form):
    ID = forms.IntegerField()
    Start = forms.IntegerField()
    Finish = forms.IntegerField()
    Step = forms.IntegerField()

class HostelForm(forms.Form):
    ID = forms.IntegerField()
    Place = forms.IntegerField()
    Faculty = forms.CharField(max_length=10)


class RoomForm(forms.Form):
    ID_Student = forms.IntegerField()
    ID_Hostel = forms.IntegerField()
    Number = forms.CharField(max_length=10)
    Sex = forms.CharField(max_length=5)
    #Room_fk = forms.ForeignKey(HostelModel)


class StudentForm(forms.Form):
    ID = forms.IntegerField()
    ID_Hostel = forms.IntegerField()
    #ID_Hostel=forms.ForeignKey(HostelModel)
    Name = forms.CharField(max_length=100)
    Surname = forms.CharField(max_length=100)
    Faculty = forms.CharField(max_length=10)
    Group = forms.CharField(max_length=10)
    Support = forms.CharField(max_length=1000)
    Sex = forms.CharField(max_length=5)
    Room = forms.CharField(max_length=10)
    #Room=forms.ForeignKey(RoomModel)
