from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.accounts.forms import RegisterForm
from django.shortcuts import render_to_response,redirect,render
from django.template import Context, RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



class HomePage(TemplateView):
    template_name='home.html'

def register(request):
    template_name='register.html'
    form=RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            password=request.POST.get('pass')
            form.save(password=password)
            messages.success(request,"User Registration Successfull,Please Login")
            return redirect('/login/')
        else:
            form=RegisterForm(request.POST)
            print "error",form.errors
    return render_to_response(template_name,{'form':form},context_instance=RequestContext(request))


def user_login(request):
    template_name='login.html'
    message=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        messages.success(request,"Invalid Username or Password")
        if user is not None:
            if user.is_active:
                    login(request, user)
                    return redirect('/passport/')
            else:
                messages.success(request,"Your account is not activated yet, please check your email")
    return render_to_response(template_name,{'message':message},context_instance=RequestContext(request),)

@login_required
@csrf_exempt
def logout_view(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect('/')

class Passport(TemplateView):
    template_name='profile.html'
