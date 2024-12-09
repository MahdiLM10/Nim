from django import forms
from .models import Profile,Ticket
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=30,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'نام',})
    )
    email = forms.EmailField(
        label="",
        required=True,
        widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'})
    )
    username = forms.CharField(
        label="",
        max_length=20,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'نام کاربری',})
    )
    password1 = forms.CharField(
        label="",
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'رمز','type':'password','name':'password'})
    )
    password2 = forms.CharField(
        label="",
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'تکرار رمز','type':'password','name':'password'})
    )

    class Meta:
        model = User
        fields = ('first_name','email', 'username', 'password1', 'password2')


# class TicketForm(forms.ModelForm):
#     Text = forms.CharField(
#         label='',
#         widget=forms.TextInput(
#             attrs={'class':'form-control width','placeholder':'توضیحات'}
#         )
#     )
#     Image = forms.ImageField(
#         label='',
#         required=False,
#     )
#     class Meta:
#         model = Poshtibani
#         fields = ('Text','Image')



class TicketForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'موضوع تیکت'}
        )
    )
    description = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class':'form-control width','placeholder':'توضیحات'}
        )
    )
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        


class UpdateUserInfo(forms.ModelForm):
    email = forms.EmailField(
        label="",
        required=True,
        widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'})
    )
    phone = forms.CharField(
        label="",
        required=False,
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره همراه'})
    )
    address1 = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'آدرس اول'})
    )
    address2 = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'})
    )
    city = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'شهر'})
    )
    state = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'منطقه'})
    )
    zipcode = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'کد پستی'})
    )


    class Meta:
        model = Profile 
        fields = ['email','phone','address1','address2','city','state','zipcode']


    
class UpdateViews(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=30,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'نام'})
    )
    username = forms.CharField(
        label="",
        max_length=20,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'نام کاربری'})
    )
    class Meta:
        model = User
        fields = ('first_name', 'username',)

    
class LostPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password','type':'password','name':'password'})
    )
    new_password2 = forms.CharField(
        label="",
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Again Password','type':'password','name':'password'})
    )
    class Meta:
        model = User
        fields = ['new_password1','new_password2']
        
        
        
class ChangePasswordForm(forms.ModelForm):
    email = forms.EmailField(
        label="",
        required=True,
        widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'})
    )
    class Meta:
        model = User
        fields = ('email',)
        
    

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(
#         label="",
#         max_length=30,
#         widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'نام',})
#     )
#     username = forms.CharField(
#         label="",
#         max_length=20,
#         widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'نام کاربری',})
#     )
#     password1 = forms.CharField(
#         label="",
#         widget= forms.PasswordInput(
#             attrs={'class': 'form-control', 'placeholder': 'رمز','type':'password','name':'password'})
#     )
#     password2 = forms.CharField(
#         label="",
#         widget= forms.PasswordInput(
#             attrs={'class': 'form-control', 'placeholder': 'تکرار رمز','type':'password','name':'password'})
#     )

#     class Meta:
#         model = User
#         fields = ('first_name', 'username', 'password1', 'password2')
        
    