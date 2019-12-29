from django.views.generic import CreateView, FormView

from .forms import LoginForm, RegisterForm
from market.mixins import RequestFormAttachMixin


# Create your views here.
class LoginView(RequestFormAttachMixin, FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'
    default_next = '/'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/'
