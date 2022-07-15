from urllib import response
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import *
import requests

def home(request):
  response=requests.get('https://fakestoreapi.com/products').json()
  return render(request, 'home.html', {'response':response})

def contact(request):
  if request.method == "POST":
    message_name = request.POST['message-name']
    message_email = request.POST['message-email']
    message = request.POST['message']

    #send mail
    send_mail(
      message_name, # subject
      message, # message
      message_email, # from email
      ['axionultra@gmail.com','geraldlayderos202@gmail.com'], # to email
    )


    return render(request,'contact.html',{'message_name' : message_name})
  else:
    return render(request,'contact.html',{})

def about(request):
  return render(request, 'about.html', {})


def product(request):
  response=requests.get('https://fakestoreapi.com/products').json()
  return render(request, 'product.html', {'response':response})

def appointment(request):
  form = BookAppointmentForm()
  if request.method == "POST":
    form = BookAppointmentForm(request.POST)
    if form.is_valid():
      form.save()
      
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    your_phone = request.POST['your-phone']
    your_email = request.POST['your-email']
    service_required = request.POST['service-required']
    your_schedule = request.POST['your-schedule']
    your_date = request.POST['your-date']
    your_message =  request.POST['your-message']

    

    #send mail
    appointment = "Name:"+ first_name + last_name + "Phone:" + your_phone +  "Email:" + your_email  + "Service Required:" + service_required + "Appointment Time:" + your_schedule + "Appointment Day:" + your_date  +  "Message:" + your_message

    
    send_mail(
      'Appointment Request', # subject
      appointment, # message
      your_email, # from email
      ['axionultra@gmail.com','geraldlayderos202@gmail.com'], # to email
    )

    
    return render(request,'appointment.html',{
      'first_name' : first_name,
      'last_name' : last_name,
      'your_phone' : your_phone,
      'your_email' : your_email,
      'service_required' :service_required,
      'your_schedule' : your_schedule,
      'your_date' : your_date,
      'your_message' : your_message,
      'form':form
      })
  else:
    return render(request,'home.html',{})

def FAQs(request):
  return render(request, 'FAQs.html', {})
