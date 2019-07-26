from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from user.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserUpdateForm
from .mixins import GroupRequiredMixin


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    queryset = User.objects.all()
    paginate_by = 15


@method_decorator(login_required, name='dispatch')
class UserCreateView(SuccessMessageMixin, GroupRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_add.html'
    success_url = '/users/'
    success_message = 'Successfully Created'
    group_required = ['admin']

    def get(self, request, *args, **kwargs):
        context = {'form': UserForm()}
        return render(request, 'user/user_add.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.set_password(user.password)
            user.save()
            return redirect('users')
        else:
            return render(request, 'user/user_add.html', {'form': form, })


@method_decorator(login_required, name='dispatch')
class UserUpdateView(SuccessMessageMixin, GroupRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/user_update.html'
    context_object_name = 'user'
    success_url = '/'
    success_message = 'Successfully Updated User'
    group_required = ['admin']


@method_decorator(login_required, name='dispatch')
class UserDeleteView(SuccessMessageMixin, GroupRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users')
    template_name = 'user/user_confirm_delete.html'
    success_message = 'Successfully deleted'
    group_required = ['admin']


@login_required
def search(request):
    user_list = User.objects.all()
    if 'user' in request.GET:
        users = request.GET['user']
        if users:
            user_list = user_list.filter(username__icontains=users)
    context = {
        'users_result': user_list,
        'values': request.GET,
    }
    return render(request, 'user/search.html', context)