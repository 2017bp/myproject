from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import Posting, Founder
from .forms import PostForm
# Create your views here.
# def index(request):
#     postings_list = Posting.objects.all()
#     context = {'postings_list': postings_list}
#     return render(request, 'BP/index.html', context)

# def detail(request, posting_id):
# 	try:
#             posting = Posting.objects.get(pk=posting_id)
# 	except Posting.DoesNotExist:
#     	    raise Http404("Posting does not exist")
# 	return render(request, 'BP/detail.html', {'posting': posting})

# def submit(request):
# 	return HttpResponse("Submit your job posting here")

class IndexView(generic.ListView):
    template_name = 'BP/index.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
        return Posting.objects.all()


class DetailView(generic.DetailView):
    model = Posting
    template_name = 'BP/detail.html'

def submit(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('http://127.0.0.1:8000/BP/')
    else:
        form = PostForm()
    return render(request, 'BP/submit_post.html', {'form': form})

