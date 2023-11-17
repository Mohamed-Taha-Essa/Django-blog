from django.shortcuts import render ,redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    post =Post.objects.all()
    context={'post_list' :post}
    return render(request ,'posts/post_list.html',context)

def post_detail(request ,pk):
    post =Post.objects.get(id =pk)
    context={'post' :post}

    return render(request ,'posts/post_detail.html',context)

## apply crud operation 
def create_post(request):
    if request.method =='POST' :
        form =PostForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/post_list/')
    else:
        form = PostForm()

    return render(request ,'posts/post_form.htm' ,{"form" :form})

def updat_post(request,pk):
    post =Post.objects.get(id=pk)
    if request.method =='POST' :
        form =PostForm(request.POST ,request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/post_list/')
    else:
        form = PostForm(instance=post)

    return render(request ,'posts/update_post.htm' ,{"form" :form})


def delet_post(request,pk):
    post =Post.objects.get(id=pk)
    if request.method == 'POST':
        # Assuming you have a confirmation step before deletion
        post.delete()
        # Redirect to a success URL after deletion
        return redirect('/post_list/')# Replace 'success_url_name' with your actual URL name
    else:
        # Handle the case where it's not a POST request, maybe show a confirmation page
        return render(request, 'posts/confirm_delete.html', {'post': post})
    


##CBV

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView


class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'  # Replace with your template name

class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'  # Replace with your template name

class PostCreate(CreateView):
    model = Post
    fields = '__all__'  # Fields to be displayed in the form
    template_name = 'posts/post_form.html'  # Replace with your template name
    success_url = reverse_lazy('post_list')  # Replace 'post_list' with your URL name for post list

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'  # Fields to be displayed in the form
    template_name = 'psots/post_update.html'  # Replace with your template name
    success_url = reverse_lazy('post_list')  # Replace 'post_list' with your URL name for post list

class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/confirm_delete.html'  # Replace with your template name
    success_url = reverse_lazy('post_list')  # Replace 'post_list' with your URL name for post list
