from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserForm
from .models import User


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {
        'users': users
    })


def detail(request, slug):
    user = get_object_or_404(User, slug=slug)
    return render(request, 'detail.html', {
        'user': user
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'form.html', {
                'form': form
            })
    else:
        form = UserForm()

        return render(request, 'form.html', {
            'form': form
        })


@login_required
def update(request, slug):
    user = get_object_or_404(User, slug=slug)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'form.html', {
                'form': form
            })
    else:
        form = UserForm(instance=user)

        return render(request, 'form.html', {
            'form': form
        })


@login_required
def delete(request, slug):
    user = get_object_or_404(User, slug=slug)
    user.delete()
    return redirect('index')
