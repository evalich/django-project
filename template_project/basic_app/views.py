from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # dicti = {'text':'hello world','number':100}
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url.html')

def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Check, if picture was sent with the form
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors(),profile_form.errors())
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                             'profile_form': profile_form,
                             'registered':registered})

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active!')
        else:
            print('User: {} and pwd {} not active!'.format(username,password))
    else:
        return render(request,'basic_app/login.html')
