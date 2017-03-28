from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import Posting, Founder
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'BP/index.html'
    context_object_name = 'postings_list'
    redirect_field_name = 'home'
    def get_queryset(self):
        return Posting.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Posting
    template_name = 'BP/detail.html'

@login_required
def submit(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/BP/')
    else:
        form = PostForm()
    return render(request, 'BP/submit_post.html', {'form': form})

@login_required
def AboutView(request):
    return render(request, 'BP/about.html', )

def logout_view(request):
    logout(request)
    return redirect('login/')

