from django.db import models
from django.core.validators import RegexValidator

class BookAppointment(models.Model): 
  first_name = models.CharField(max_length=60, null = True)
  last_name = models.CharField(max_length=60, null = True)
  phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, null = True)
  email = models.CharField(max_length=60, null = True)
  day = models.CharField(max_length=60, null = True)
  time = models.CharField(max_length=60, null = True)
  service = models.CharField(max_length=60, null = True)
  message = models.CharField(max_length=60, null = True)

  date_created = models.DateTimeField(auto_now_add = True, null = True, blank=True)

  def __str__(self):
    return (self.first_name, self.last_name)