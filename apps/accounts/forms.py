from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from models import Campground

class RegisterForm(forms.ModelForm):
    fname=forms.CharField(max_length=100)
    lname=forms.CharField(max_length=100)
    uname=forms.CharField(max_length=100)
    term_condition=forms.BooleanField()

    class Meta:
        model = User
        exclude=['date_joined','token','last_login','username','password']


    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError(("User with this email already exists please try another."))
        if email == "":
            raise forms.ValidationError(("This field is required."))
        return email

    def clean_term_condition(self):
        term_condition = self.cleaned_data.get("term_condition")
        if term_condition == False:
            raise forms.ValidationError(_("Please Select Terms and condition"))
        return term_condition

    def save(self, **kwargs):
        password = kwargs.pop('password', False)
        details=super(RegisterForm,self).save(commit=False)
        print "ssss",self.cleaned_data.get('username')
        username=self.cleaned_data.get('username')
        return details
        details.username=self.cleaned_data.get('uname')
        details.first_name=self.cleaned_data.get('fname')
        details.last_name=self.cleaned_data.get('lname')
        details.set_password(password)
        details.email=self.cleaned_data.get('email')
        details.is_active=True
        details.save()
        return details


class CampgroundModelForm(forms.ModelForm):

    class Meta:
        model = Campground
        exclude = ['user', 'timestamp']
