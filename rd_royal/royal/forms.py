from django.shortcuts import redirect, render
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})