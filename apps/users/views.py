from django.shortcuts import render
from django.views.generic import FormView, TemplateView, DeleteView, View, CreateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Usuario

from braces.views import LoginRequiredMixin

class PanelTV(LoginRequiredMixin, TemplateView):
    template_name = "users/panel.html"
    login_url = reverse_lazy('users_login')

class LoginTV(TemplateView):
    template_name = "users/login.html"


class LoginFormView(FormView):
    #form_class = RegistroForm
    #template_name = 'accounts/register.html'
    success_url = reverse_lazy('users_panel')  # por ahora redirije a esta pagina (iteracion1)

    def post(self, request, *args, **kwargs):
        print request.POST, "<--registro--"
        try:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            if username and password:
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(self.success_url)
                else:
                    messages.error(request, 'username y/o password incorrectos')
                    return HttpResponseRedirect(reverse_lazy('users_login'))
            else:
                messages.error(request, 'username y password requiridos')
                return HttpResponseRedirect(reverse_lazy('users_login'))
        except Exception, e:
            print e, "<-- Error --"
            messages.error(request, 'Ocurrio un error')
            return HttpResponseRedirect(reverse_lazy('users_login'))


class RegisterTV(TemplateView):
    template_name = "users/register.html"

class RegisterFormView(FormView):
    #form_class = RegistroForm
    #template_name = 'accounts/register.html'
    success_url = reverse_lazy('users_login')  # por ahora redirije a esta pagina (iteracion1)

    def post(self, request, *args, **kwargs):
        print request.POST, "<--registro--"
        try:
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)

            if username and password and email:
                user = User()
                user.username = username
                user.set_password(password)
                user.save()

                usuario = Usuario.objects.create(user=user, email=email)
                return HttpResponseRedirect(reverse_lazy('users_login'))
            else:
                messages.error(request, 'Todos los datos son requiridos')
                return HttpResponseRedirect(reverse_lazy('users_login'))
        except Exception, e:
            print e, "<-- Error --"
            messages.error(request, 'Ocurrio un error')
            return HttpResponseRedirect(reverse_lazy('users_register'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('users_login'))