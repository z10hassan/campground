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



class HomePage(TemplateView):
    template_name='home.html'


#class Register(TemplateView):
#    template_name='register.html'
#    form_class = RegisterForm
#
#    def get(self, request, *args, **kwargs):
#        form = self.form_class()
#        return render(request, self.template_name, {'form': form})
#
#    def post(self, request, *args, **kwargs):
#        form=self.form_class()
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Successfully Registered')
#            return redirect('/')
#        else:
#            print "gggggggggggggggggggggggggggggggggggggggggg",form.errors
#            return render_to_response(self.template_name,{'form':form},context_instance=RequestContext(request))
#        print "ddd",form.errors
#        return render_to_response(self.template_name,{'form':form},context_instance=RequestContext(request))

def register(request):
    template_name='register.html'
    form=RegisterForm
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        print "error",form.errors
        return render_to_response(self.template_name,{'form':form},context_instance=RequestContext(request))


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
                    return redirect('/')
            else:
                messages.success(request,"Your account is not activated yet, please check your email")
    return render_to_response(template_name,{'message':message},context_instance=RequestContext(request),)



class CreateCampgroundView(CreateView):
    """
    create consultant basic dettails 
    """

    template_name = 'list-campground.html'
    form_class = CampgroundModelForm

    def form_valid(self, form):
        print ">>>>>>>>>>>>>>>>>>>"
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

