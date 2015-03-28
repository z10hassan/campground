from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        exclude=['date_joined','token','last_login']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


    def save(self, **kwargs):
        details=super(RegisterForm,self).save(commit=False)
        print "ssss",self.cleaned_data.get('username')
        username=self.cleaned_data.get('username')
        return details