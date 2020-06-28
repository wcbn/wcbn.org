from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import User
from .forms import CreateUserForm


class WCBNLoginView(LoginView):
    title = 'Log In'

    def get(self, request, *args, **kwargs):
        if (request.GET.get('next', None)):
            if request.user.is_authenticated:
                messages.error(request, 'You are not authorized to view this content.')
            else:
                messages.info(request, 'Please log in to view this page.')
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx


class UserCreateView(CreateView):
    template_name = 'users/create.html'
    model = User
    title = 'Join'
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('/') #TODO

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['SHOULD_RELOAD'] = True
        return ctx

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/') #TODO
        return super().get(self, request)


    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            new_user = authenticate(email=email, password=password)
            login(request, new_user)

            msg = EmailMessage(
                subject='Welcome to WCBN',
                body=f'Hi {first_name},\nThanks for signing up!',
                to=[email]
            )
            msg.send()
            return redirect('/') #TODO

        return super().post(request)
