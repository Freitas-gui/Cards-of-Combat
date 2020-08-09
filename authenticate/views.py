import sweetify
from django.shortcuts import render
from django.views.generic import CreateView

from .form import userSignUpForm
from .models import User


class UserSignUp(CreateView):
    model = User
    form_class = userSignUpForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()


    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
        errorResponse = "deu erro"
        sweetify.error(self.request, errorResponse, persistent='Ok')

        return response