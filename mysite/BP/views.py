from django.http import HttpResponse
from django.shortcuts import render

from .models import Posting
# Create your views here.
def index(request):
    postings_list = Posting.objects.all()
    context = {'postings_list': postings_list}
    return render(request, 'BP/index.html', context)

def detail(request, posting_id):
	try:
            posting = Posting.objects.get(pk=posting_id)
	except Posting.DoesNotExist:
    	    raise Http404("Posting does not exist")
	return render(request, 'BP/detail.html', {'posting': posting})

def submit(request):
	return HttpResponse("Submit your job posting here")