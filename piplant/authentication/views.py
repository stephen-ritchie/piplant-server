from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from .forms import LoginForm


class UserLoginFormView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next', None) # here method should be GET or POST.
        if next_url:
            return "%s" % (next_url) # you can include some query strings as well
        else :
            return reverse('home') # what url you wish to return

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, 'Invalid credentials. Please try again.')

        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect(UserLoginFormView.as_view())


