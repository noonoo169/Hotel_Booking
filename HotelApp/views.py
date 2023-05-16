from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .import models
from .forms import Online_Booking_form,offline_Booking_form,Add_Room_form
from django.http import HttpResponse


# Create your views here.
def home(request):  
    if 'user_id' in request.session:
        id = request.session['user_id']
        print(id)
        author  = models.Authorregis.objects.filter(Id=id).first()
        return render(request,'Home.html', {'Name' : author.Fname })
    print("No")
    return render(request,'Home.html')

def all(request):
    return render(request,'allinclude.html')

def userLogin(request):
    if request.method == 'POST':
        User_email = request.POST.get('Email')
        User_password = request.POST.get('Password')
        my_user = authenticate(username = User_email, password=User_password)
        author  = models.Authorregis.objects.filter(Email=User_email, Password=User_password).first()
        if my_user is not None :
            login(request, my_user)
            return redirect("adminHome")
        elif author:
            request.session['user_id'] = author.Id
            return redirect("home")
        else:
            messages.success(request, 'user name and password not matching')
            return render(request,'Login.html')
    return render(request,'Login.html')

def userLogout(request):
    if 'user_id' in request.session:
        del request.session["user_id"]
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
    
def registerAccount(request):
    if request.method == 'POST':
        Data = models.Authorregis()
        Data.Fname = request.POST.get('Fname')
        Data.Lname = request.POST.get('Lname')
        Data.Email = request.POST.get('Email')
        Data.Phone_Number = request.POST.get('Phone_Number')
        Data.Password = request.POST.get('Password')
        Con_password = request.POST.get('Con_password')
        if Data.Password == Con_password:
            Data.save()
            return redirect('userLogin')
        else:
           return HttpResponse('password and confirm password not matching')
    return render(request,'RegisterAccount.html')

def forgetPassword(request):
    return render(request,'ForgetPassword.html')

def all_admin(request):
    return render(request,'admin/AdminAllinclude.html')

def adminHome(request):
    if request.user.is_authenticated:
        data = models.Online_Booking.objects.all().order_by('-Id')
        return render(request,'admin/AdminHome.html',{'data':data})
def createOnlineBooking(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            isValidRoom = models.Add_Room.objects.filter(Is_Available=True, Room_Type=request.POST.get('Select_Room')).first()
            if isValidRoom:
                MyData = models.Online_Booking()
                MyData.Id = request.POST.get('Id')
                customer = models.Authorregis.objects.get(Id=request.session['user_id'])
                MyData.Customer_id = customer.Id
                MyData.Check_in = request.POST.get('Check_in')
                MyData.Check_out = request.POST.get('Check_out')
                MyData.First_Name = request.POST.get('First_Name')
                MyData.Last_Name = request.POST.get('Last_Name')
                MyData.Email = request.POST.get('Email')
                MyData.Phone_Number = request.POST.get('Phone_Number')
                MyData.Address = request.POST.get('Address')
                MyData.Country = request.POST.get('Country')
                MyData.Personal_Identity = request.POST.get('Personal_Identity')
                MyData.Select_Room = request.POST.get('Select_Room')
                MyData.Room_Number = isValidRoom.Room_Number
                MyData.Image = request.FILES.get('Image')
                MyData.ADULT = request.POST.get('ADULT')
                MyData.CHILDREN = request.POST.get('CHILDREN')
                MyData.Date = request.POST.get('Date')
                MyData.Time = request.POST.get('Time')
                MyData.save()
                models.Add_Room.objects.filter(Id=isValidRoom.Id).update(Is_Available=False)
                return redirect('home')
            else:
                return HttpResponse("No more room for this type")
        else:
            print(request.session['user_id'])
            Room_Type_value = request.GET.get('id')
            Room = models.Add_Room.objects.filter(Room_Type= Room_Type_value).first()
            return render(request,'BookingRoom.html',{'Room':Room})
    return redirect('userLogin')

def onlineBookingInfor(request):
    if request.method == 'POST':
        value = request.POST.get('search')
        print(value)
        show = models.Online_Booking.objects.filter(Country =value) or models.Online_Booking.objects.filter(First_Name=value)
        return render(request,'admin/OnlineBooking.html',{"data":show})

    data = models.Online_Booking.objects.all().order_by('-First_Name')
    return render(request,'admin/OnlineBooking.html',{'data':data})

def editOnlineBooking(request,id):
    data = models.Online_Booking.objects.get(Id=id)
    print(id)
    if request.method == 'POST':
        customer = models.Authorregis.objects.get(Id = request.POST.get('Customer_Id'))
        data.Customer = customer
        data = Online_Booking_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('onlineBookingInfor')
        else:
            return HttpResponse("Failed")
    return render(request,'admin/EditOnlineBooking.html',{'data': data})

def deleteOnlineBooking(request,id):
    data = models.Online_Booking.objects.get(Id=id)
    models.Add_Room.objects.filter(Room_Number=data.Room_Number).update(Is_Available=True)
    data.delete()
    return redirect('onlineBookingInfor')

def addCustomer(request):
    if request.method == 'POST':
        isValidRoom = models.Add_Room.objects.filter(Is_Available=True, Room_Type=request.POST.get('Select_Room')).first()
        if isValidRoom:
            Data = models.Offline_Booking()
            Data.Check_in = request.POST.get('Check_in')
            Data.Check_out = request.POST.get('Check_out')
            Data.First_Name = request.POST.get('First_Name')
            Data.Last_Name = request.POST.get('Last_Name')
            Data.Email = request.POST.get('Email')
            Data.Phone_Number = request.POST.get('Phone_Number')
            Data.ADULT = request.POST.get('ADULT')
            Data.CHILDREN = request.POST.get('CHILDREN')
            Data.Select_Room = request.POST.get('Select_Room')
            Data.Room_Number = isValidRoom.Room_Number
            Data.Personal_Identity = request.POST.get('Personal_Identity')
            Data.Image = request.FILES.get('Upload_Image')
            Data.Country = request.POST.get('Country')
            Data.Address = request.POST.get('Address')
            Data.Date = request.POST.get('Date')
            Data.Time = request.POST.get('Time')
            Data.save()

            models.Add_Room.objects.filter(Id=isValidRoom.Id).update(Is_Available=False)
            return redirect('AddCustomer')
        else:
            return HttpResponse("No more room for this type")

    data = models.Offline_Booking.objects.all().order_by('-Id')
    return render(request,'admin/AddCustomer.html',{'data': data})

def allCustomer(request):
    if request.method == 'POST':
        value = request.POST.get('search')
        if value == "":
            data = models.Offline_Booking.objects.all().order_by('-First_Name')
        else:
            data = models.Offline_Booking.objects.filter(First_Name=value) or models.Offline_Booking.objects.filter(Select_Room=value)
        return render(request, 'admin/AllCustomer.html', {"data": data})
    data = models.Offline_Booking.objects.all().order_by('-First_Name')
    return render(request,'admin/AllCustomer.html',{'data': data})

def editCustomer(request,id):
    data = models.Offline_Booking.objects.get(Id=id)
    if request.method == 'POST':
        data = offline_Booking_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('AllCustomer')
        else:
            return HttpResponse("Failed")
    return render(request,'admin/EditCustomer.html',{'data': data})

def AddCustpage_Delete(request,id):
    data = models.Offline_Booking.objects.get(Id=id)
    models.Add_Room.objects.filter(Room_Number=data.Room_Number).update(Is_Available=True)
    data.delete()
    return redirect('AddCustomer')

def AllCustpage_Delete(request,id):
    data = models.Offline_Booking.objects.get(Id=id)
    models.Add_Room.objects.filter(Room_Number=data.Room_Number).update(Is_Available=True)
    data.delete()
    return redirect('AllCustomer')

def addRoom(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('Room_Image')
        if request.method == 'POST':
            Data = models.Add_Room()
            Data.Room_Number = request.POST.get('Room_Number')
            Data.Room_Type = request.POST.get('Room_Type')
            Data.Room_Floor = request.POST.get('Room_Floor')
            Data.Room_Facility = request.POST.get('Room_Facility')
            Data.Room_Price = request.POST.get('Room_Price')
            Data.Is_Available = True
            Data.Room_Image = upload_image
            Data.Date = request.POST.get('Date')
            Data.Time = request.POST.get('Time')
            Data.save()
            return redirect('addRoom')
        else:
            return HttpResponse("Failed")

    data = models.Add_Room.objects.all().order_by('-Room_Number')
    return render(request, 'admin/AddRoom.html',{'data': data})

def addRoomSearch(request):
    if request.method == 'POST':
        Serch = request.POST.get('serch')
        print(Serch)
        data = models.Add_Room.objects.filter(Room_Number=Serch) or models.Add_Room.objects.filter(Room_Type=Serch)
        return render(request, 'admin/AddRoom.html',{"data": data})

def AddRooms_Delete(request,id):
    data = models.Add_Room.objects.get(Id=id)
    data.delete()
    return redirect('addRoom')

def editRoom(request,id):
    data = models.Add_Room.objects.get(Id=id)
    if request.method == 'POST':
        data = Add_Room_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('allRoom')
        else:
            return HttpResponse("Failed")

    isAvailable = data.Is_Available
    if isAvailable == True:
        isAvailable = 1
    else:
        isAvailable = 0

    roomType = data.Room_Type
    if roomType == 'Single':
        roomType = 1
    elif roomType == 'Double':
        roomType = 2
    elif roomType == 'Family':
        roomType = 3
    elif roomType == 'Luxury':
        roomType = 4
    elif roomType == 'Delux':
        roomType = 5
    else:
        roomType = 6


    floor = data.Room_Floor
    if floor == 'Floor_First':
        floor = 1
    elif floor == 'Floor_Second':
        floor = 2
    elif floor == 'Floor_Third':
        floor = 3
    else:
        floor = 4

    return render(request,'admin/EditRoom.html',{'data': data,
                                                 "isAvailable": isAvailable,
                                                 "roomType": roomType,
                                                 "floor": floor
                                                 })

def allRoom(request):
    if request.method == 'POST':
        Serch = request.POST.get('search')
        if Serch == "":
            data = models.Add_Room.objects.all().order_by('-Id')
        else:
            data = models.Add_Room.objects.filter(Room_Number=Serch) or models.Add_Room.objects.filter(Room_Type=Serch)
        return render(request, 'admin/AllRooms.html',{"data": data})

    data = models.Add_Room.objects.all().order_by('-Id')
    return render(request, 'admin/AllRooms.html',{'data': data})

def AllRooms_Delete(request,id):
    data = models.Add_Room.objects.get(Id=id)
    data.delete()
    return redirect('allRoom')

