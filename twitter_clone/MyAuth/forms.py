from registration.forms import RegistrationForm
from MyAuth.models import MyUser

class MyUserForm(RegistrationForm):
     class Meta:
         model = MyUser
         fields = ['username', 'email', 'password1', 'password2']
