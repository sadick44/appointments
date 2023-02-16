from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Appointment


def home(request):

    return render(request, "home.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
            else:
                messages.warning(request, "Votre email ou mot de passe est incorrect")
    return render(request, "registration_forms/login.html", {"name": "name"})


def user_register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            if User.objects.filter(username=form.cleaned_data['email']).exists():
                messages.warning(request, "Vous avez deja un compte avec cet email")

            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                messages.warning(request, "Les deux mots de passe ne sont pas identiques")

            else:
                user = User.objects.create_user(username=form.cleaned_data['email'],
                                                        first_name=form.cleaned_data['first_name'],
                                                last_name=form.cleaned_data['last_name'],
                                                        password=form.cleaned_data['password1'])
                user.save()
                return redirect(request.GET.get('next', '/'))

    return render(request, 'registration_forms/signup.html', {'form': form})


@login_required(login_url='/login')
def take_appointment(request):
    adminUsers = User.objects.filter(is_staff=True).exclude(username="admin")
    if request.method == 'POST':
        appointement_date = request.POST['appointment']
        appointement_date = datetime.strptime(appointement_date, '%Y-%m-%dT%H:%M')
        user_id = User.objects.get(username=request.user).id

        if Appointment.objects.filter(user_id=user_id, appointement_date=appointement_date).exists():
             messages.warning(request, "Cette date est prise")

        else:
            time_appointment = appointement_date.time()
            time_appointment = datetime.strptime(time_appointment.strftime("%H:%M"),"%H:%M")

            #check whether the given time is less than 9:30 or greather than 17:30

            if time_appointment < datetime.strptime("09:00", "%H:%M") or time_appointment > datetime.strptime("17:00", "%H:%M"):
                messages.warning(request, "Vous pouvez prendre rendez-vous que, après 9H30 et avant 17h30")
            # check whether the appointement day is weekend or not

            elif appointement_date < datetime.now():
                messages.warning(request, "Vous ne pouvez pas rendre des dates passées")
                print(appointement_date.weekday(), type(appointement_date.weekday()))

            elif appointement_date.weekday() > 5:
                messages.warning(request, "Vous ne pouvez pas prendre de rendez vous pendant le week-end")
            else:
                user_appointment = Appointment.objects.create(user_id=user_id,
                                                              appointement_date=appointement_date,
                                                              )
                user_appointment.save()
                messages.success(request, "Votre rendez-vous est pris en compte")

    return render(request, "appointment.html", {"users": adminUsers})