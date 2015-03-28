from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.accounts.forms import RegisterForm
from django.shortcuts import render_to_response,redirect,render
from django.template import Context, RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login



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
    if form.is_valid()
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