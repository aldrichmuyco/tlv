import uuid
from django.db import models

# Create your models here.
class Province(models.Model):    
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=10)


class City(models.Model):    
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    city = models.BooleanField(default=False)
    zip_code = models.CharField(max_length=10)


class Profile(models.Model):
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widowed'),
    )

    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=True, default="")
    middle_name = models.CharField(max_length=50, blank=True, default="")
    last_name = models.CharField(max_length=50, blank=True, default="")
    extension = models.CharField(max_length=16, blank=True, default="")

    gender = models.CharField(max_length=15, choices=GENDER)
    nationality = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=24, choices=MARITAL_STATUS, blank=True)

    address_1 = models.CharField(max_length=255, blank=True, default="")
    address_2 = models.CharField(max_length=255, blank=True, default="")
    province = models.ForeignKey(Province, related_name="provinces", on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, related_name="cities", on_delete=models.DO_NOTHING)
    country = models.CharField(max_length=100, default="Philippines")

    contact_no = models.CharField(max_length=16, blank=True, default="")
    is_guest = models.BooleanField(default=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    
    def __str__(self):
        return '%s, %s %s' % (self.last_name, self.first_name, self.middle_name)


class Membership(models.Model):    
    membership_id = models.CharField(max_length=50, blank=True, default="")
    membership_date = models.DateField(auto_now=False, auto_now_add=False)
    profile = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="", null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)