from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from .forms import PublicationForm, UserForm
from .models import UserModel, Publication, BlockedUsers


def profile(request):
    queryset1 = UserModel.objects.filter(user=request.user).all()
    queryset2 = Publication.objects.filter(user=request.user).all()
    context = {"users": queryset1, "user_publications": queryset2}
    # context = {"users": queryset1}
    return render(request, "profile.html", context=context)


def publication(request):
    queryset = Publication.objects.filter(user=request.user).exclude().all()
    context = {"publications": queryset}
    return render(request, "publications.html", context=context)


def blocked_users(request):
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            block = form_data.save(commit=False)  # za da ne se sochuva odma vo baza
            block.user = request.user
            block.save()
            return redirect("blocked_users")  # za da nema dvojno sochuvuvanje

    queryset = BlockedUsers.objects.filter(blocker=request.user).all()
    context = {"blocked_users": queryset, "form": UserForm}
    return render(request, "blocked_users.html", context=context)


def add_publications(request):
    if request.method == "POST":
        form_data = PublicationForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            add_publication = form_data.save(commit=False)  # za da ne se sochuva odma vo baza
            add_publication.user = request.user
            add_publication.save()
            return redirect("add_publications")  # za da nema dvojno sochuvuvanje

    queryset = Publication.objects.all()
    context = {"add_publications": queryset, "form": PublicationForm}
    return render(request, "add_publication.html", context=context)
