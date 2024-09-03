from django.shortcuts import render
from complaints.models import Complaint
from complaints.forms import ComplaintForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def index(request):
    context = {} 
    form = ComplaintForm()
    context['form'] = form
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            print(form)
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.image = request.FILES.get('image')
            complaint.save()
            context['msg'] = 'Complaint registered successfully'
        else:
            return HttpResponse(form.errors)
    return render(request, 'complaints/complain.html', context)


def signup(request):
    context = {}
    form = CustomUserCreationForm()
    context['form'] = form
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context['msg'] = 'User registered successfully'
        else:
            context['msg'] = 'Invalid data'
    return render(request, 'registration/signup.html', context)

def listComplaints(request):
    context = {}
    context['active_complaints'] = Complaint.objects.filter(action_taken=False)
    context['closed_complaints'] = Complaint.objects.filter(action_taken=True)
    return render(request, 'complaints/home.html', context)
