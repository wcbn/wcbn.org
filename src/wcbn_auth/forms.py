from django.contrib.auth.forms import UserCreationForm
from .models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']

    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-callback': 'enableFormSubmit'
            }
        ),
        label=''
    )

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.pop('autofocus')

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
