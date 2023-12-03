from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required

@login_required
def post_created(request):
    if request.method=="POST":
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            new_item=form.save(commit=False,files=request.FILES)
            new_item.user=request.user
            new_item.save()

    else:
        form=PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})