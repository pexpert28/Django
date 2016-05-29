from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext, render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import View, ListView
from Shelegram.forms import RegistrationForm;
from Shelegram.models import ShelegramUser
from django.contrib.auth import logout
from Shelegram.models import ShelegramUser, ShelegramGroup

def index(request):
    return render(request, 'shelegram/index.html', {})

# def login(request):
#     return render(request, 'shelegram/login.html', {})


class Register(View):
    user_model_register_form = RegistrationForm()
    template_name = 'shelegram/register.html'

    def get(self, request, *args, **kwargs):
        context = RequestContext(request)
        return render_to_response(self.template_name,
                                  {'user_model_register_form': self.user_model_register_form,
                                   'registered': False},
                                  context)

    def post(self, request, *args, **kwargs):
        registered = False
        context = RequestContext(request)
        user_model_register_form = RegistrationForm(data=request.POST)
        if user_model_register_form.is_valid():
            user = user_model_register_form.save()
            user.set_password(user.password)
            if 'picture' in request.FILES:
                user.picture = request.FILES['picture']
            user.save()
            registered = True
        return render_to_response(self.template_name,
                                  {'user_model_register_form': user_model_register_form,
                                   'registered': registered},
                                  context)
                                  
class CreateGroup(View):
    group_creation_form = GroupCreationForm()
    template_name = 'shelegram/createGroup.html'

    def get(self, request, *args, **kwargs):
        context = RequestContext(request)
        return render_to_response(self.template_name,
                                  {'group_creation_form': self.group_creation_form,
                                   'created': False},
                                  context)

    def post(self, request, *args, **kwargs):
        created = False
        context = RequestContext(request)
        group_creation_form = GroupCreationForm(data=request.POST)
        if group_creation_form.is_valid():
            user = ShelegramUser.objects.get(pk=request.user.pk)
            group = group_creation_form.save()
            group.admin = user
            if 'picture' in request.FILES:
                group.picture = request.FILES['picture']
            group.save()
            created = True
        return render_to_response(self.template_name,
                                  {'group_creation_form': group_creation_form,
                                   'created': created},
                                  context)
                                  
                                  
def profile(request):
    try:
        logged_in = ShelegramUser.objects.get(username = request.user)
    except:
        logout(request)
        return HttpResponseRedirect('/')
    return render(request, 'shelegram/profile.html', {'user': logged_in})

