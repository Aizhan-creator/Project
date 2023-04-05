
from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=16)

    def __str__(self) :
        return self.name
    
class Cinema(models.Model):
    name = models.CharField(max_length=64)
    total_cinema_halls = models.IntegerField()
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name    

class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    total_seats = models.IntegerField()
    cinema = models.ForeignKey(to=Cinema, on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
    
class CinemaSeat(models.Model):
    cinema_hall = models.ForeignKey(to=CinemaHall, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    type = models.IntegerField(enumerate)
    
    def __str__(self) :
        return self.id
    
class ShowSeat(models.Model):
    status = models.IntegerField(enumerate)
    price = models.IntegerField()
   #  cinema_seat = models.ForeignKey()
    def __str__(self) :
        return self.id
    


class Show(models.Model):
    date = models.DateField()
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self) :
        return self.id

class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    duration = models.DateField()
    language = models.CharField(max_length=16)
    release_date = models.DateField()
    country = models.CharField(max_length=64)
    genre = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.title

class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=16)
   
    def __str__(self) :
         return self.name
    
class Booking(models.Model):
    name = models.ForeignKey(to=User, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    time_stamp = models.DateField()
    status = models.IntegerField(enumerate)

    def __str__(self) :
        return self.name    
class Payment(models.Model):
    amount = models.IntegerField()
    timestamp = models.DateField()
    discount_coupon = models.IntegerField()
    remote_transaction = models.IntegerField()
    payment_method = models.IntegerField(enumerate)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
