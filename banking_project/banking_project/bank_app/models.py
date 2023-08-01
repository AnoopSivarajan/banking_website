from django.db import models


# Create your models here.
class District(models.Model):
    district = models.CharField(max_length=250)
    wiki_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.district


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class UserData(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')])
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=150, choices=[('Savings Account', 'Savings Account'),
                                                             ('Current Account', 'Current Account'),
                                                             ('NRI Account', 'NRI Account')])

    def __str__(self):
        return self.name
