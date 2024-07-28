from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone


class School(models.Model):
    school_name = models.CharField(max_length=255)
    school_mobile_1 = models.CharField(max_length=15)
    school_mobile_2 = models.CharField(max_length=15, blank=True, null=True)
    school_mobile_3 = models.CharField(max_length=15, blank=True, null=True)
    school_whatsapp_number = models.CharField(max_length=15)
    school_email_id = models.EmailField()
    school_address = models.TextField()

    principal_name = models.CharField(max_length=255)
    principal_mobile_number = models.CharField(max_length=15)
    principal_email_id = models.EmailField()
    principal_address = models.TextField()

    director_name = models.CharField(max_length=255)
    director_mobile_number = models.CharField(max_length=15)
    director_email_id = models.EmailField()
    director_address = models.TextField()

    dean_name = models.CharField(max_length=255)
    dean_mobile_number = models.CharField(max_length=15)
    dean_email_id = models.EmailField()
    dean_address = models.TextField()

    school_photo = models.ImageField(upload_to='school_photos/')
    address = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name


class Parent(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    user_mobile1 = models.CharField(max_length=15)
    user_mobile2 = models.CharField(max_length=15, blank=True, null=True)
    user_mobile3 = models.CharField(max_length=15, blank=True, null=True)
    user_email_id = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    payment_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user_name

    def generate_payment_link(self):
        unique_id = get_random_string(length=32)
        self.payment_link = f"http://yourdomain.com/payment/{unique_id}"
        self.save()


class Payment(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    transaction_id = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.parent.user_name} - {self.transaction_id}'


class Kid(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    kid_class = models.CharField(max_length=20)
    roll_number = models.IntegerField()
    enrollment_number = models.IntegerField()
    photo = models.ImageField(upload_to='kids_photos/')
    disability = models.BooleanField(default=False)
    disabled_part = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    fees_status = models.CharField(max_length=50)
    monthly_fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
