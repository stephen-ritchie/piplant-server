from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from oauth2_provider.decorators import protected_resource
from django.contrib.auth.decorators import login_required

from .forms import UserForm

@login_required()
def home(request):
    return render(request, 'core/index.html')

class NewUserFormView(FormView):
    template_name = 'core/new_user_form.html'
    form_class = UserForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        email = form.cleaned_data.get('email', '')
        password = form.cleaned_data.get('password', '')
        user = User.objects.create_user(username=email, email=email, password=password)
        print("Create user: %s" % user.get_username())
        return super().form_valid(form)


@login_required()
def profile_view(request):
    return render(request, 'core/profile.html', {'user': request.user})



