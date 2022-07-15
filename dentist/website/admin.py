from django.contrib import admin
from .forms import BookAppointmentForm
from .models import BookAppointment

class BookAppointmentAdmin(admin.ModelAdmin):
   list_display = ['first_name','last_name','phone','email','day','time', 'service', 'message']
   form = BookAppointmentForm
   list_filter = ['first_name', 'last_name']
   search_fields = ['first_name', 'last_name']

admin.site.register(BookAppointment,BookAppointmentAdmin)

