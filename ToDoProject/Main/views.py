from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Work

# Create your views here.
@login_required
def index(request):
    total_completed = Work.objects.filter(author=request.user, is_completed=True).count()
    total = Work.objects.filter(author=request.user).count()
    return render(request, template_name="Main/index.html", context={
        "total_completed": total_completed,
        "total": total,
        "not_completed": total - total_completed,
    })


class CreateWork(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Work
    fields = ['title', 'description', 'priority', 'complete_till', 'is_completed']
    template_name = "Main/add_work.html"
    success_message = "Work was added successfully"

    def get_success_url(self) -> str:
        return reverse("main:work_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WorkList(LoginRequiredMixin, ListView):
    model = Work
    template_name = "Main/worklist.html"
    paginate_by = 25

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)       

class WorkUpdate(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Work
    template_name = "Main/updatework.html"
    fields = ['title', 'description', 'priority', 'complete_till', 'is_completed']
    success_message = "Work was updated successfully"
    
    def get_success_url(self):
        return reverse("main:work_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class WorkDelete(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Work
    success_message = "Work was deleted successfully"

    def get_success_url(self):
        return reverse("main:work_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False