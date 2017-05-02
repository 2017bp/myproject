from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import Posting, Founder, UserProfile, Company
from .forms import PostForm, UserForm, CompanyForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'BP/index.html'
    context_object_name = 'postings_list'
    redirect_field_name = 'home'
    def get_queryset(self):
        return Posting.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Posting
    template_name = 'BP/detail.html'


class StudentDirectoryView(LoginRequiredMixin, generic.ListView):
    template_name = 'BP/student_directory.html'
    context_object_name = 'user_profiles_list'
    def get_queryset(self):
        return UserProfile.objects.all()

class CompanyDirectoryView(LoginRequiredMixin, generic.ListView):
    template_name = 'BP/company_directory.html'
    context_object_name = 'company_list'
    def get_queryset(self):
        return Company.objects.all()


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
    company_count = Company.objects.count()
    student_count = UserProfile.objects.count()
    posting_count = Posting.objects.count()
    return render(request, 'BP/about.html', {'company_count':company_count, 'student_count':student_count, 'posting_count':posting_count})

def logout_view(request):
    logout(request)
    return redirect('login/')

@login_required
def delete_posting(request, post_id):
    posting = Posting.objects.get(pk=post_id)
    if request.user == posting.user:
        Posting.objects.filter(id=post_id).delete()
        return redirect('/BP/')
    else:
        raise PermissionDenied 



# referenced from https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/
@login_required() # only logged in users should access this
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('website', 'blurb', 'city', 'country', 'major', 'interested_in_joining_a_startup'))
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

@login_required() # only logged in users should access this
def edit_company(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, Company, fields=('company_name', 'company_description', 'company_link', 'company_founders', 'company_contact_info', 'display_in_company_directory'))
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

        return render(request, "BP/company_info_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

