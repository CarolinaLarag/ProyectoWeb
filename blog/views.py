from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Post, Proveedor
from .forms import PostForm, ProveedorForm


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)
    return render(request, 'blog/index.html', {'posts': posts})

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