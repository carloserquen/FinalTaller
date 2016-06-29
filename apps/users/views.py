from django.shortcuts import render
from django.views.generic import FormView, TemplateView, DeleteView, View, CreateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

class PanelTV(TemplateView):
    template_name = "users/panel.html"


class LoginTV(TemplateView):
    template_name = "users/login.html"
    success_url = reverse_lazy('users_panel')


class RegisterTV(TemplateView):
    template_name = "users/register.html"
    success_url = reverse_lazy('users_login')