from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from .models import CustomUser  

class SignupUserForm(UserCreationForm):  
    class Meta:  
        model = CustomUser  
        fields = ('email', 'full_name')  

class ProfileForm(forms.ModelForm):  
    class Meta:  
        model = CustomUser  
        fields = ('first_name', 'last_name', 'address', 'tel')  
        widgets = {  
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),  
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),  
            'address': forms.TextInput(attrs={'class': 'form-control'}),  
            'tel': forms.TextInput(attrs={'class': 'form-control'}),  
        }