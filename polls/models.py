import datetime
from django.db import models
from django.utils import timezone


#In fields we can give the null=True, It is directly related into DB and also we can store "null" values in DB
#blank= True it is directly related to the Django project, here we can store the empty string in 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Product(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

    # 2023 - 0
    # 8 - 25
    # 10: 00
    # AM

class Email(models.Model):
    from_email = models.EmailField(help_text="From Email")
    to_email = models.EmailField(help_text="To Email")
    subject = models.CharField(max_length=500)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject


class CustomerDetails(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(primary_key=True, max_length=20)
    email = models.EmailField()
    test_drive_timing = models.DateTimeField()
    location = models.CharField(max_length=100)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)

class Dealer(models.Model):
    dealer_location = models.CharField(max_length=100)
    customers = models.ManyToManyField(CustomerDetails)
    dealer_name = models.CharField(max_length=100)
    dealer_code = models.IntegerField()
    dealer_mobile=models.IntegerField(default=10)

    def __str__(self):
        return self.dealer_location