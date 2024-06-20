from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from typing import Any

# Formulário de autenticação(login).
class LoginForm(AuthenticationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Inicializa o formulário de login e configura o helper do crispy-forms.

        Args:
            *args: Argumentos posicionais.
            **kwargs: Argumentos nomeados.
        """
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_show_errors = False
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary mt-1'))
