from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignUpForm(UserCreationForm):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    INTEREST_CHOICES = (
        ("1", "Python"),
        ("2", "Golang"),
        ("3", "SQL"),
        ("4", "Docker"),
        ("5", "Azure"),
        ("6", "FastAPI"),
        ("7", "Django"),
        ("8", "Flask"),
    )
    phone = forms.CharField(max_length=12)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    interests = forms.MultipleChoiceField(choices = INTEREST_CHOICES)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['username'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})

        # giving place holders to fields
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Enter Your Username*'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Enter Your Email*'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password'})

        for text in ['username', 'password1', 'password2']:
            self.fields[text].help_text = None
