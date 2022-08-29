from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from django.views.generic import ListView
from blog.models import Posts


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} your account has been created')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    
    return render(request,'users/register.html',{'form':form})

def profile(request):
    return render(request,'users/profile.html')


class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name: 'posts'