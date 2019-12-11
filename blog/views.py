from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.utils import timezone
from .models import Post, Proveedor
from .forms import PostForm, ProveedorForm


# Create your views here.

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
               
                return redirect('/')

    return render(request, "blog/login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/')

def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        print(posts)
        return render(request, 'blog/index.html', {'posts': posts})
    return redirect('/login')

def nosotros(request):
    return render(request, 'blog/nosotros.html')

def contactanos(request):
    return render(request, 'blog/contactanos.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def proveedores(request):
    provs = Proveedor.objects.all()
    print(provs)
    return render(request, 'blog/proveedores.html', {'provs': provs})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def proveedor_detail(request, pk):
    prov = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'blog/proveedor_detail.html', {'prov': prov})

def post_new(request):
    		form = PostForm()
    		return render(request, 'blog/post_edit.html', {'form': form})

def proveedor_new(request):
    		form = ProveedorForm()
    		return render(request, 'blog/proveedor_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def proveedor_new(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            prov = form.save(commit=False)      
            prov.save()
            
            return redirect('proveedor_detail', pk=prov.pk)
    else:
        form = ProveedorForm()
    return render(request, 'blog/proveedor_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def proveedor_edit(request, pk):
    prov = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=prov)
        if form.is_valid():
            prov = form.save(commit=False)
            prov.save()
            return redirect('proveedor_detail', pk=prov.pk)
    else:
        form = ProveedorForm(instance=prov)
    return render(request, 'blog/proveedor_edit.html', {'form': form})