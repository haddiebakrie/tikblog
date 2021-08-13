from django.shortcuts import redirect, render
from .form import RegistrationForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from blog.models import Post

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have Successfully registered.')
            return redirect('feed')
    else:
        form = RegistrationForm()
    return render(request, 'blog/anonymous/register.html', {'form':form})

def profile(request):
    c_user = request.user
    posts = Post.objects.filter(author=c_user.id)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    return render(request, "blog/member/me.html", {'user':c_user, 'profile_form':profile_form, 'posts':posts})

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, f"You are now logged in as {username}")
                login(request, user)
                return redirect('feed')
            else:
                messages.info(request, f"Invalid uername or password.")
        else:
                messages.info(request, f"Invalid uername or password.")
    form = AuthenticationForm()
    return render(request, 'blog/member/login.html', {'form':form})

