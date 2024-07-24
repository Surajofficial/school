from django.db import models
from django.utils.crypto import get_random_string


class School(models.Model):
    name = models.CharField(max_length=255)
    school_mobile1 = models.CharField(max_length=15)
    school_mobile2 = models.CharField(max_length=15, blank=True, null=True)
    school_mobile3 = models.CharField(max_length=15, blank=True, null=True)
    school_email_id = models.EmailField()
    principle_name = models.CharField(max_length=255)
    director_name = models.CharField(max_length=255)
    dean_name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


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
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[(
        'pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent.user_name} - {self.amount}"


class Kid(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[(
        'male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    disability = models.BooleanField(default=False)
    disability_part = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
