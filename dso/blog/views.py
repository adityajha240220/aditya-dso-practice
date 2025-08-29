# Write the view code that checks if the form is valid and saves the data.

from django.shortcuts import render
from .forms import UserForm

def user_form_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully")
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})