from django.shortcuts import redirect, render
from .models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def inquiry(request):
  if request.method == 'POST':
      car_id = request.POST['car_id']
      car_title = request.POST['car_title']
      user_id = request.POST['user_id']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      customer_needs = request.POST['customer_need']
      email = request.POST['email']
      phone = request.POST['phone']
      message = request.POST['message']
      city = request.POST['city']

      if request.user.is_authenticated:
          user_id = request.user.id
          has_contacted = contact.objects.all().filter(car_id=car_id, user_id=user_id)
          if has_contacted:
              messages.error(request, 'You are alrady made this inquiry of this car.')
              return redirect('/cars/'+car_id)

      contacts = contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_needs=customer_needs, email=email, phone=phone, message=message, city=city)

      

      admin_info = User.objects.get(is_superuser =True)
      admin_email = admin_info.email

      send_mail(
          'New Car Inquiry.',
          'You have a new inquiry' + car_title + '. Please check your Dashboard.',
          'AnytimeFreelancing2k20@gmail.com',
          [admin_email],
          fail_silently=False,
        )

      contacts.save()
      messages.success(request, 'Your request has been submitted!')
      return redirect('/cars/'+car_id) 