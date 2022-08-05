from django.shortcuts import render
from django.http import HttpResponse
import smtplib
import json
from decouple import config

USER_EMAIL= config('USER_EMAIL')
USER_PASSWORD= config('USER_PASSWORD')


# Create your views here.
def index(request):
    # global details= dict()
    email= request.POST.get('user_mail')
    message= request.POST.get('user_msg')
    connection= smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user= user_email, password= user_password)

    subject="Email automation part1 "
    message="Hey everyone in this first part"
    final= f"Subject:{subject}\n \n{message}"

    connection.sendmail(from_addr=user_email, to_addrs="joblesscoder2468@gmail.com", msg=final)

    connection.close()
    return render(request, "single/index.html")

def result(request):
    # var_name= details['your_name']
    # global details
    print(details['name'])
    return render(request, "single/result.html", name= details['name'])
