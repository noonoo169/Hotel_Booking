from django import forms
from .import models

class Online_Booking_form(forms.ModelForm):
    class Meta:
        model = models.Online_Booking
        fields = ["Id", "Check_in", "Check_out", "First_Name", "Last_Name", "Email", "Phone_Number", "ADULT", "CHILDREN", "Image", "Address", "Country" ]

class offline_Booking_form(forms.ModelForm):

 
    class Meta:
        model = models.Offline_Booking
        fields = "__all__"

class Add_Room_form(forms.ModelForm):
    class Meta:
        model = models.Add_Room
        fields = "__all__"



