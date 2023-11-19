from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets

class LoginUserForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
class ChangePasswordUserForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
         self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
         self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class": "form-control"})


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required = True

    def clenan_email(self):
        email=self.cleaned_data.get("email")
        if User.object.filter(email=email).exists():
            self.add_error("email","E-Mail daha önce kullanılmış.")
        return email


