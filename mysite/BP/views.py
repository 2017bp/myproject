from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import Posting, Founder, UserProfile
from .forms import PostForm, UserForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

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
            post.user = request.user
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

@login_required() # only logged in users should access this
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/BP')

        return render(request, "BP/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


