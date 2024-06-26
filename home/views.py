from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Update
from .forms import UpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """ A view to return the index page """
    update = Update.objects.all()

    context = {
        'update': update,
    }
    
    return render(request, 'home/index.html', context)


@login_required
def edit_update(request):
    """ Edit the update """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    update = get_object_or_404(Update)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited update!')
            return redirect(reverse('edit_update'))
        else:
            messages.error(request, 'Failed to edit update. Please ensure the form is valid.')
    else:
        form = UpdateForm(instance=update)
        messages.info(request, f'You are editing the update')

    template = 'home/edit_home.html'
    context = {
        'form': form,
        'update': update,
    }

    return render(request, template, context)


