from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации с дополнительными полями."""

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "example@mail.com"
        })
    )
    phone_number = forms.CharField(
        required=False,
        max_length=20,
        label="Номер телефона",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+7 (999) 123-45-67"
        })
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите имя пользователя"
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите пароль"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Подтвердите пароль"
        })

    def clean_email(self):
        """Проверка уникальности email."""
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Пользователь с таким email уже существует."
            )
        return email
