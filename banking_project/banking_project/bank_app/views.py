from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import District,Branch,UserData
from django.http import JsonResponse


# Create your views here.
def home(request):
    districts = District.objects.all()
    return render(request, "home.html", {'districts': districts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password1 == password:
            if User.objects.filter(username=username):
                messages.info(request, "Username already taken")
            else:
                user = User.objects.create_user(username=username, password=password, )
                user.save()
                messages.info(request, "User Created")
                return redirect('/login/')

        else:
            messages.info(request, "Password Missmatch")

    districts = District.objects.all()
    return render(request, "register.html", {'districts': districts})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Successfully longed in')
        else:
            messages.info(request, 'invalid credentials')

    districts = District.objects.all()
    return render(request, "login.html", {'districts': districts})


def welcome(request):
    districts = District.objects.all()
    return render(request, "welcome.html", {'districts': districts})


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district_id = request.POST['district']
        branch_id = request.POST['branch']
        account_type = request.POST['account_type']

        district = District.objects.get(pk=district_id)
        branch = Branch.objects.get(pk=branch_id)

        user_data = UserData(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type
        )
        user_data.save()

        return redirect('/')

    districts = District.objects.all()
    return render(request, 'form.html',{'districts': districts})

from django.http import JsonResponse

def get_branches_by_district(request, district_id):
    try:
        district = District.objects.get(pk=district_id)
        branches = Branch.objects.filter(district=district)
        data = [{'id': branch.id, 'name': branch.name} for branch in branches]
        return JsonResponse(data, safe=False)
    except District.DoesNotExist:
        return JsonResponse([], safe=False)


def logout(request):
    auth.logout(request)
    return redirect('/')

