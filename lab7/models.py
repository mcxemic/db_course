from django.db import models
from django.db.models import F


# Create your models here.
class loopModel(models.Model):
    Number = models.IntegerField()
    Start = models.IntegerField()
    Finish = models.IntegerField()
    Step = models.IntegerField()


class HostelModel(models.Model):
    ID = models.PositiveIntegerField()
    Place = models.PositiveIntegerField()
    Faculty = models.CharField(max_length=10)

    def __str__(self):
        return " Hostel number {0} of faculty: {1}. With {2} empty place. ".format(self.ID, self.Faculty, self.Place)


class RoomModel(models.Model):
    ID_Student = models.CharField(max_length=100)
    ID_Hostel = models.PositiveIntegerField()
    Number = models.CharField(max_length=10)
    Sex = models.CharField(max_length=5)
    Room_fk = models.ForeignKey(HostelModel)

    def __str__(self):
        return 'Room number {0} in {1} '.format(self.Number,self.ID_Hostel)


class StudentModel(models.Model):
    ID = models.CharField(max_length=10)
    #ID_Hostel = models.PositiveIntegerField()
    ID_Hostel=models.ForeignKey(HostelModel)
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Faculty = models.CharField(max_length=10)
    Group = models.CharField(max_length=10)
    Support = models.CharField(max_length=1000)
    Sex = models.CharField(max_length=5)
    #Room = models.CharField(max_length=10)
    Room=models.ForeignKey(RoomModel)

    def __str__(self):
        return '{0} {1} in faculty {2}. Group {3}'.format(self.Name,self.Surname,self.Faculty,self.Group)

    def save(self, *args,**kwargs):
        p=HostelModel.objects.get(id=self.ID_Hostel.ID)
        p.Place-=1
        p.save()
        #HostelModel.objects.get(id=self.ID_Hostel.ID).update(Place=F('Place')+1)
        #super(StudentModel,self).save(*args,**kwargs)

