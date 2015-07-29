from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(verbose_name="Country Name", max_length = 100, unique =True, help_text="Enter Name of the country here")
    code = models.CharField(max_length = 20, unique= True)
    def __str__(self):
        return self.code
    class Meta:
        verbose_name_plural = 'Countries'

class State(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 5)
    def __str__(self):
        return self.country.code + ' > ' + self.name

class City(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length = 100)

class Profile(models.Model):
    account = models.OneToOneField(User, primary_key = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    following = models.ManyToManyField(User, related_name = 'followers')
    city = models.ForeignKey(City, blank=True, null=True)
    street_address = models.CharField(max_length = 100, default = '')
    def __str__(self):
        return self.account.username




