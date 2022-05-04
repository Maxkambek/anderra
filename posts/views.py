from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment,Category,Tag
from .forms import CreatePostForm


def home_view(request):
    objects=Post.objects.order_by('-id')
    last_3_post = Post.objects.order_by('-id')[:3]
    comments=Comment.objects.all()
    categories=Category.objects.all()
    q=request.GET.get('q')
    cat=request.GET.get('cat')
    tags=Tag.objects.all()
    tag=request.GET.get('tag')

    if tag:
        objects=objects.filter(tag__tags__exact=tag)
    if cat:
        objects=objects.filter(category__title__exact=cat)
    if q:
        objects=objects.filter(title__icontains=q)
    context={
        'object_list':objects,
        'comments':comments,
        'categories':categories,
        'tags':tags,
        'last_3_post': last_3_post,
    }

    return render(request,'posts/index.html',context)


def fashion_view(request):
    articles = Post.objects.all()
    print(articles)

    context = {
        'objects': articles
    }

    return render(request, 'posts/fashion.html', context)


def travel_view(request):
    articles = Post.objects.order_by('-id').filter(category__title__exact='TRAVEL')

    context = {
        'objects': articles
    }

    return render(request, 'posts/travel.html', context)


def post_detail_view(request,slug):
    post=get_object_or_404(Post,slug=slug)
    form=CreatePostForm()
    categories=Category.objects.all()
    tags=Tag.objects.all()
    comments=Comment.objects.order_by('-id')

    if request.method=="POST":
        form=CreatePostForm(request.POST ,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('/')

    context={
        'object':post,
        'categorirs':categories,
        'tags':tags,
        'form':form,
        'comments':comments,
    }
    return render(request,'posts/single.html',context)


def about_view(request):
    return render(request, 'posts/about.html')




