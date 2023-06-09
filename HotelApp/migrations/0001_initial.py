# Generated by Django 4.1.3 on 2023-05-11 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Add_Room",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Room_Number", models.CharField(max_length=255, unique=True)),
                ("Room_Type", models.CharField(max_length=255)),
                ("Room_Floor", models.CharField(max_length=255)),
                ("Room_Facility", models.CharField(max_length=500)),
                ("Room_Price", models.CharField(max_length=255)),
                ("Room_Image", models.ImageField(upload_to="")),
                ("Is_Available", models.BooleanField(default=True)),
                ("Date", models.DateField(auto_now_add=True)),
                ("Time", models.TimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Add_Room",
            },
        ),
        migrations.CreateModel(
            name="Authorregis",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Fname", models.CharField(max_length=255)),
                ("Lname", models.CharField(max_length=255)),
                ("Email", models.CharField(max_length=255, unique=True)),
                ("Role", models.CharField(max_length=255)),
                ("Phone_Number", models.IntegerField()),
                ("Password", models.CharField(max_length=255)),
                ("Date", models.DateField(auto_now_add=True)),
                ("Time", models.TimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Authority_reg",
            },
        ),
        migrations.CreateModel(
            name="Offline_Booking",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Check_in", models.CharField(max_length=255)),
                ("Check_out", models.CharField(max_length=255)),
                ("First_Name", models.CharField(max_length=255)),
                ("Last_Name", models.CharField(max_length=255)),
                ("Email", models.CharField(max_length=255)),
                ("Phone_Number", models.IntegerField()),
                ("Address", models.CharField(max_length=255)),
                ("Country", models.CharField(max_length=255)),
                ("Personal_Identity", models.CharField(max_length=255)),
                ("Image", models.ImageField(upload_to="")),
                ("ADULT", models.CharField(max_length=255)),
                ("CHILDREN", models.CharField(max_length=255)),
                ("Select_Room", models.CharField(max_length=255)),
                ("Room_Number", models.CharField(max_length=255)),
                ("Date", models.DateField(auto_now_add=True)),
                ("Time", models.TimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Offline_Booking_Customer",
            },
        ),
        migrations.CreateModel(
            name="OrderRoom",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Check_in", models.CharField(max_length=255)),
                ("Check_out", models.CharField(max_length=255)),
                ("First_Name", models.CharField(max_length=255)),
                ("Last_Name", models.CharField(max_length=255)),
                ("Email", models.CharField(max_length=255)),
                ("Phone_Number", models.IntegerField()),
                ("Address", models.CharField(max_length=255)),
                ("Country", models.CharField(max_length=255)),
                ("Personal_Identity", models.CharField(max_length=255)),
                ("ADULT", models.CharField(max_length=255)),
                ("CHILDREN", models.CharField(max_length=255)),
                ("Select_Room", models.CharField(max_length=255)),
                ("Room_Number", models.CharField(max_length=255)),
                ("Date", models.DateField(auto_now_add=True)),
                ("Time", models.TimeField(auto_now_add=True)),
                ("Total_Price", models.FloatField()),
                ("Is_Pay", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "OrderRoom",
            },
        ),
        migrations.CreateModel(
            name="Online_Booking",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Check_in", models.CharField(max_length=255)),
                ("Check_out", models.CharField(max_length=255)),
                ("First_Name", models.CharField(max_length=255)),
                ("Last_Name", models.CharField(max_length=255)),
                ("Email", models.CharField(max_length=255)),
                ("Phone_Number", models.IntegerField()),
                ("Address", models.CharField(max_length=255)),
                ("Country", models.CharField(max_length=255)),
                ("Personal_Identity", models.CharField(max_length=255)),
                ("Image", models.ImageField(upload_to="")),
                ("ADULT", models.CharField(max_length=255)),
                ("CHILDREN", models.CharField(max_length=255)),
                ("Select_Room", models.CharField(max_length=255)),
                ("Room_Number", models.CharField(max_length=255)),
                ("Date", models.DateField(auto_now_add=True)),
                ("Time", models.TimeField(auto_now_add=True)),
                (
                    "Customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HotelApp.authorregis",
                    ),
                ),
            ],
            options={
                "db_table": "Online_Booking_table",
            },
        ),
    ]
