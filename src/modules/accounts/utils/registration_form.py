from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from typing import Any

# Formulário de registro de usuário que utiliza crispy-forms para estilização.
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Inicializa o formulário de registro e configura o helper do crispy-forms.

        Args:
            *args: Argumentos posicionais.
            **kwargs: Argumentos nomeados.
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
