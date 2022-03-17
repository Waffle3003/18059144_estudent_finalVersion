from asyncio.windows_events import NULL
from doctest import Example
from email.policy import default
from queue import Empty
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum


#class User(models.Model):
    #userID = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=15)
    #password = models.CharField(max_length=64)
    #email_address = models.CharField(max_length=64)
    #user_date_created = models.DateTimeField(default=timezone.now)

    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    budget = models.FloatField(null=True, blank=True, default=None)
    needs = models.FloatField(null=True, blank=True, default=None)
    wants = models.FloatField(null=True, blank=True, default=None)
    savings = models.FloatField(null=True, blank=True, default=None)
    edit_date_budget = models.DateTimeField(default=timezone.now)

    class Meta:
        get_latest_by = ['user']

    def __str__(self):
       return str(self.user)


class Need(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    needs_budget = models.FloatField(null=True, blank=True, default=None)
    rent_accomodation = models.FloatField(null=True, blank=True, default=None)
    food = models.FloatField(null=True, blank=True, default=None)
    utility_bills = models.FloatField(null=True, blank=True, default=None)
    mobile_phone = models.FloatField(null=True, blank=True, default=None)
    compulsory_course_expenses = models.FloatField(null=True, blank=True, default=None)
    compulsory_travel = models.FloatField(null=True, blank=True, default=None)
    other_needs = models.FloatField(null=True, blank=True, default=None)
    edit_date_needs = models.DateTimeField(default=timezone.now)
    total_left_needs = models.FloatField(null=True, blank=True, default=None)
    leftover_need_budget = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
       return str(self.user)

    def save(self):
        self.total_left_needs = self.rent_accomodation + self.food + self.utility_bills + self.mobile_phone + self.compulsory_course_expenses + self.compulsory_travel + self.other_needs
        self.leftover_need_budget = self.needs_budget - self.total_left_needs
        return super(Need, self).save()

class Want(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    wants_budget = models.FloatField(null=True, blank=True, default=None)
    going_out = models.FloatField(null=True, blank=True, default=None)
    takeaway = models.FloatField(null=True, blank=True, default=None)
    unnecessary_transport = models.FloatField(null=True, blank=True, default=None)
    clothes_personal_care = models.FloatField(null=True, blank=True, default=None)
    other_wants = models.FloatField(null=True, blank=True, default=None)
    edit_date_wants = models.DateTimeField(default=timezone.now)
    total_left_wants = models.FloatField(null=True, blank=True, default=None)
    leftover_want_budget = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
       return str(self.user)

    def save(self):
        self.total_left_wants = self.going_out + self.takeaway + self.unnecessary_transport + self.clothes_personal_care + self.other_wants 
        self.leftover_want_budget = self.wants_budget - self.total_left_wants
        return super(Want, self).save()


class Saving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    savings_budget = models.FloatField(null=True, blank=True, default=None)
    savings_used = models.FloatField(null=True, blank=True, default=None)
    edit_date_savings = models.DateTimeField(default=timezone.now)
    month_int = models.IntegerField(null=True, blank=True, default=None)
    total_left_savings = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
       return str(self.user)

    def save(self):
        self.total_left_savings = self.savings_budget - self.savings_used
        return super(Saving, self).save()


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id = models.AutoField(auto_created = True, primary_key=True, default=None)
    name = models.CharField(null=True, blank=True, default=None, max_length=60)
    amount = models.FloatField(null=True, blank=True, default=None)
    date_due = models.DateField(null=True, blank=True, default=None, help_text = "Please format YY-MM-DD")

    def __str__(self):
       return str(self.user) + str(self.name)

    def myprop(self):
        myproperty = "Hello there property"
        return myproperty


    


