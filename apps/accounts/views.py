from django.views.generic.edit import (CreateView, UpdateView, DeleteView, View, FormView)
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from apps.accounts.forms import RegisterForm
from django.shortcuts import render_to_response,redirect,render
from django.template import Context, RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from models import Campground
from forms import (CampgroundModelForm)
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


class CreateCampgroundView(CreateView):
    """
    create Campground basic dettails 
    """

    template_name = 'list-campground.html'
    form_class = CampgroundModelForm

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form_data = form.save(commit=False)
        form_data.user = self.request.user
        form_data.save()
        form = CampgroundModelForm()
        msg = "successfully registered"
        return self.render_to_response(self.get_context_data(form=form,success=msg))
