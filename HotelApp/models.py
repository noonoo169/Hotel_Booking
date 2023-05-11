from django.db import models

# Create your models here.
class Authorregis(models.Model):
    Id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique=True)
    Role = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    Password = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Fname
    class Meta:
        db_table = 'Authority_reg'

class Add_Room(models.Model):
    Id = models.AutoField(primary_key=True)
    Room_Number = models.CharField(max_length=255,unique=True)
    Room_Type = models.CharField(max_length=255)
    Room_Floor = models.CharField(max_length=255)
    Room_Facility = models.CharField(max_length=500)
    Room_Price = models.CharField(max_length=255)
    Room_Image = models.ImageField(upload_to='')
    Is_Available = models.BooleanField(default=True)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Room_Number
    class Meta:
        db_table = 'Add_Room'

class Online_Booking(models.Model):
    Id = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(Authorregis,on_delete=models.CASCADE)
    Check_in = models.CharField(max_length=255)
    Check_out = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Personal_Identity = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='')
    ADULT = models.CharField(max_length=255)
    CHILDREN = models.CharField(max_length=255)
    Select_Room = models.CharField(max_length=255)
    Room_Number = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Name
    class Meta:
        db_table = 'Online_Booking_table'

class Offline_Booking(models.Model):
    Id = models.AutoField(primary_key=True)
    Check_in = models.CharField(max_length=255)
    Check_out = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Personal_Identity = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='')
    ADULT = models.CharField(max_length=255)
    CHILDREN = models.CharField(max_length=255)
    Select_Room = models.CharField(max_length=255)
    Room_Number = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.First_Name
    class Meta:
        db_table = 'Offline_Booking_Customer'

class OrderRoom(models.Model):
    Id = models.AutoField(primary_key=True)
    Check_in = models.CharField(max_length=255)
    Check_out = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Personal_Identity = models.CharField(max_length=255)
    ADULT = models.CharField(max_length=255)
    CHILDREN = models.CharField(max_length=255)
    Select_Room = models.CharField(max_length=255)
    Room_Number = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    Total_Price = models.FloatField()
    Is_Pay = models.BooleanField(default=False)
    def __str__(self):
        return self.First_Name
    class Meta:
        db_table = 'OrderRoom'




