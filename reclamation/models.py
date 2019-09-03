from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    basic_info = models.OneToOneField(User, on_delete=models.CASCADE)


class Company(models.Model):
    basic_info = models.OneToOneField(User, on_delete=models.CASCADE)
    post_code = models.CharField(max_length=6, default="none")
    city = models.CharField(max_length=64, default="none")
    street = models.CharField(max_length=64, default="none")
    number = models.CharField(max_length=16, default="none")
    company_number = models.IntegerField(unique=True, default=0)  # NIP


class Branch(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    number = models.CharField(max_length=16)
    post_code = models.CharField(max_length=6)
    phone_number = models.IntegerField(unique=True)
    employee = models.ManyToManyField(Employee)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def show_branch(self):
        return f"{self.city}, {self.street}, {self.number}"


class Client(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=128, unique=True)
    phone_number = models.CharField(max_length=9, unique=True)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}"


class Producer(models.Model):
    name = models.CharField(max_length=32, unique=True)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    symbol = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=16)
    price = models.FloatField()
    producer = models.ManyToManyField(Producer)

    def __str__(self):
        return f"{self.name}"


status_list = (
    (0, "Przyjęta"),
    (1, "Wysłana do producenta"),
    (2, "Odpowiedź od producenta"),
    (3, "Oczekiwanie na klienta"),
    (4, "Zakończona"),
)


class Reclamation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=32, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    option_one = models.CharField(max_length=256)
    option_two = models.DateField()
    option_three = models.DateField()
    option_four = models.CharField(max_length=128)
    option_five = models.CharField(max_length=128)
    option_six = models.BooleanField()
    option_seven = models.BooleanField()
    option_eight = models.BooleanField()
    option_nine = models.BooleanField()
    status = models.IntegerField(choices=status_list, default=0)

    def show(self):
        return f"{self.client.first_name} {self.client.last_name}, {self.product}"

