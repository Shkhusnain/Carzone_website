from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
from datetime import datetime
from multiselectfield import MultiSelectField
from django.db.models.enums import Choices



# Create your models here.

class Car(models.Model):
    state_choice = (
      ('PU','Punjab'),
      ('KPK','Khyber Pakhtunkhwa'),
      ('SN','Sindh'),
      ('BL','Blochistan'),
      ('FD','Federal Territory'),
    )
    year_choice = []
    for r in range(2000,(datetime.now().year+1)):
      year_choice.append((r,r))

    features_choice = (
        ('Cruise control','Cruise control'),
        ('Audio Interface','Audio Interface'),
        ('Airbags','Airbags'),
        ('Air Conditioning','Air Conditioning'),
        ('Seat Heating','Seat Heating'),
        ('Alarm System','Alarm System'),
        ('ParkAssist','ParkAssist'),
        ('Power steering','Power steering'),
        ('Reversing Camera','Reversing Camera'),
        ('Direct fuel Injection','Direct fuel Injection'),
        ('Auto start/stop','Auto start/stop'),
        ('Wind Deflector','Wind Deflector'),
        ('Bluetooth Handset','Bluetooth Handset'),
    )
    door_choice = (
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5'),
      ('6','6'),
    )
    

    car_title=models.CharField(max_length=255)
    state=models.CharField(choices=state_choice, max_length=100)
    city=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    year=models.IntegerField(('year'),choices=year_choice)
    condition=models.CharField(max_length=255)
    price=models.IntegerField()
    description=RichTextField()
    car_photo= models.ImageField(upload_to='photots/%y/%m/%d/')
    car_photo1=models.ImageField(upload_to='photots/%y/%m/%d/', blank=True)
    car_photo2=models.ImageField(upload_to='photots/%y/%m/%d/', blank=True)
    car_photo3=models.ImageField(upload_to='photots/%y/%m/%d/', blank=True)
    car_photo4=models.ImageField(upload_to='photots/%y/%m/%d/', blank=True)
    features=MultiSelectField(choices=features_choice, max_length=100)
    body_style=models.CharField(max_length=255)
    engine=models.CharField(max_length=255)
    transmission=models.CharField(max_length=255)
    interior=models.CharField(max_length=255)
    miles=models.IntegerField()
    doors=models.CharField(choices=door_choice, max_length=100)
    passengers=models.CharField(max_length=255)
    vin_no=models.CharField(max_length=255)
    milage=models.IntegerField()
    fuel_type=models.CharField(max_length=255)
    no_of_owners=models.CharField(max_length=255)
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title 