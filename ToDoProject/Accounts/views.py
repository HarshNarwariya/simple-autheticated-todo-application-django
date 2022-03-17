from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, message=f"Account created for {username}!")
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, template_name="Accounts/register.html", context={
        "form": form,
    })