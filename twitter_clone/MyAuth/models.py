from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class MyUser(AbstractBaseUser):
    #class Meta:
        #app_label = 'MyAuth'
        #db_table = "MyUser"
    """ Got help from here
    http://blog.mathandpencil.com/replacing-django-custom-user-models-in-an-existing-application/
    """

    # Usernames can contain only A-z, 0-9 and underscore (_). This makes their
    # use more universal - they can be used automatically in urls and also typed
    # easily from any keyboard with roman/latin alphabet. These are the same
    # constraints as in the original Twitter.

    # Note that the validator will be run only when a user is saved from a ModelForm.

    username = models.CharField(max_length=15,
                                unique=True,
                                validators=[
                                RegexValidator(regex=r'^[A-Za-z0-9_]+$',
                                message="Usernames are max. 15 characters and \
                                can contain only letters (A-Z), \
                                digits and the underscore (_).",
                                code="invalid_username"),] )

    full_name = models.CharField(_('full name'), max_length=254, blank=True)
    short_name = models.CharField(_('short name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
	#is_staff = models.BooleanField(_('staff status'), default=False,
	#	help_text=_('Designates whether the user can log into this admin '
	#				'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                help_text=('Designates whether this user should be treated as '
				            'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # Username and password should not be in REQUIRED_FIELDS as they are always
    # required.
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email
