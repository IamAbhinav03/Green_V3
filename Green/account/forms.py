from django.forms import widgets
from account.models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm


# from .models import Consumer, User

# class ConsumerSignupForm(UserCreationForm):
# 	class Meta(UserCreationForm.Meta):
# 		model = User

# 	@transaction.atomic
# 	def save(self):
# 		user = super().save(commit=False)
# 		user.is_consumer = True
# 		user.save()
# 		Consumer.objects.create(user=user)
# 		return user

class NewUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'id': 'form2Example11', 'class': 'form-control', 'placeholder': 'Email'})
		self.fields['username'].widget.attrs.update({'id': 'form2Example11', 'class': 'form-control', 'placeholder': 'Username'})
		self.fields['password1'].widget.attrs.update({'id': 'form2Example22', 'class': 'form-control', 'placeholder': 'Password'})
		self.fields['password2'].widget.attrs.update({'id': 'form2Example22', 'class': 'form-control', 'placeholder': 'Confirm Password'})

	email = forms.EmailField(required=True)

	class Meta:
		model = Account
		fields = ["email", "username", "password1", "password2"]
		# widgets = {
		# 	"username": forms.CharField(widgets.TextInput(attrs={"id": "form2Example11", "class": "form-control", "placeholder": "Username"})),
		# 	"email": widgets.EmailInput(attrs={"id": "form2Example11", "class": "form-control", "placeholder": "Email"}),
		# 	"password1": widgets.TextInput(attrs={"id": "form2Example22", "class": "form-control", "placeholder": "Password"}),
		# 	"password2": widgets.TextInput(attrs={"id": "form2Example22", "class": "form-control", "placeholder": "Confirm Password"}),
		# }

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class NewStaffForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'id': 'form2Example11', 'class': 'form-control', 'placeholder': 'Email'})
		self.fields['username'].widget.attrs.update({'id': 'form2Example11', 'class': 'form-control', 'placeholder': 'Username'})
		self.fields['password1'].widget.attrs.update({'id': 'form2Example22', 'class': 'form-control', 'placeholder': 'Password'})
		self.fields['password2'].widget.attrs.update({'id': 'form2Example22', 'class': 'form-control', 'placeholder': 'Confirm Password'})

	email = forms.EmailField(required=True)

	class Meta:
		model = Account
		fields = ["email", "username", "password1", "password2", 'is_staff']
		# widgets = {
		# 	"username": forms.CharField(widgets.TextInput(attrs={"id": "form2Example11", "class": "form-control", "placeholder": "Username"})),
		# 	"email": widgets.EmailInput(attrs={"id": "form2Example11", "class": "form-control", "placeholder": "Email"}),
		# 	"password1": widgets.TextInput(attrs={"id": "form2Example22", "class": "form-control", "placeholder": "Password"}),
		# 	"password2": widgets.TextInput(attrs={"id": "form2Example22", "class": "form-control", "placeholder": "Confirm Password"}),
		# }

	def save(self, commit=True):
		print('sdfjasdlkfjasldkfjalsdk ')
		user = super(NewUserForm, self).save(commit=False)
		print(type(user))
		user.email = self.cleaned_data['email']
		user.is_staff = True
		if commit:
			user.save()
		return user

#################################################################################
# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

# User = get_user_model()

# class RegisterForm(forms.ModelForm):
#     """
#     The default 

#     """

#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email']

#     def clean_email(self):
#         '''
#         Verify email is available.
#         '''
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email

#     def clean(self):
#         '''
#         Verify both passwords match.
#         '''
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "Your passwords must match")
#         return cleaned_data


# class UserAdminCreationForm(forms.ModelForm):
#     """
#     A form for creating new users. Includes all the required
#     fields, plus a repeated password.
#     """
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email']

#     def clean(self):
#         '''
#         Verify both passwords match.
#         '''
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "Your passwords must match")
#         return cleaned_data

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ['email', 'password', 'is_active', 'admin']

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]