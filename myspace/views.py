from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post,NewsLetterRecipients,Category, update_post_id_field_in_category_model,tags,DevPost,Kategory
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from random import sample
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.http import JsonResponse

# Blog categories
def post_list_by_category(request , category_slug):
    categories = Category.objects.all()
    kategories = Kategory.objects.all()
    post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    form = NewsLetterForm()
    return render(request, 'blog/category/list_by_category.html', {'categories': categories, 'post': post, 'category': category, "letterForm":form,'kategories': kategories,})



def tagged(request,  kategory_slug, slug=None):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = DevPost.objects.filter(dev_tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'blog/category/devpost_by_category.html', context)



# Dev categories
def devpost_list_by_category(request , kategory_slug):
    # tag = get_object_or_404(Tag, slug=slug)
    categories = Category.objects.all()
    kategories = Kategory.objects.all()
    devpost = DevPost.objects.filter(status='published')
    common_tags = DevPost.dev_tags.all()
    if kategory_slug:
        kategory = get_object_or_404(Kategory, slug=kategory_slug)
        devpost = devpost.filter(kategory=kategory)
    form = NewsLetterForm()
    return render(request, 'blog/category/devpost_by_category.html', {'kategories': kategories, 'devpost': devpost, 'kategory': kategory,"letterForm":form,'categories': categories,'common_tags':common_tags,})

# Blog list view
def post_list_view(request, category_slug=None):
    categories = Category.objects.all()
    kategories = Kategory.objects.all()
    post = Post.objects.filter(status='published')
    tagz = tags.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    list_objects = Post.published.all()
    recent = Post.objects.order_by('publish')[0:5]
    paginator = Paginator(list_objects, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    form = NewsLetterForm()
    
    categorypostdictionary = {category: list(set([Post.objects.get( id=x ) for x in category.post_ids if len(category.post_ids) > 1])) for category in categories}

    twopercategory = {x: sample( categorypostdictionary[x], 2 ) for x in categorypostdictionary if len(list(set( categorypostdictionary[x]))) > 1}

    return render(request, 'blog/post/list.html', {'posts': posts,"letterForm":form, 'recent': recent, 'categories': categories, 'post': post, 'twopercategory': twopercategory, 'tagz':tagz,'kategories': kategories,})


# Dev list view
def devpost_list_view(request, kategory_slug=None):
    kategories = Kategory.objects.all()
    categories = Category.objects.all()
    devpost = DevPost.objects.filter(status='published')
    common_tags = DevPost.dev_tags.most_common()[:4]
    if kategory_slug:
        kategory = get_object_or_404(Kategory, slug=kategory_slug)
        devpost = devpost.filter(kategory=kategory)
    list_objects = DevPost.published.all()
    # recent = Post.objects.order_by('publish')[0:5]
    paginator = Paginator(list_objects, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    form = NewsLetterForm()
    
    # categorypostdictionary = {category: list(set([Post.objects.get( id=x ) for x in category.post_ids if len(category.post_ids) > 1])) for category in categories}

    # twopercategory = {x: sample( categorypostdictionary[x], 2 ) for x in categorypostdictionary if len(list(set( categorypostdictionary[x]))) > 1}

    return render(request, 'blog/post/devlist.html', {'posts': posts,"letterForm":form, 'kategories': kategories, 'devpost': devpost, 'common_tags':common_tags, 'categories': categories,})


# Blog detail view
def post_detail_view(request, year, month, day, post, category_slug=None):
    categories = Category.objects.all()
    kategories = Kategory.objects.all()
    recent = Post.objects.order_by('publish')[0:4]
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    form = NewsLetterForm()
    return render(request, 'blog/post/detail.html', {'post': post,"letterForm":form, 'categories': categories, 'recent': recent,'kategories': kategories,})

# Dev detail view
def devpost_detail_view(request, year, month, day, post, Kategory_slug=None):
    kategories = Kategory.objects.all()
    categories = Category.objects.all()
    # recent = Post.objects.order_by('publish')[0:4]
    devpost = get_object_or_404(DevPost, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    common_tags = DevPost.dev_tags.most_common()[:2]
    # if kategory_slug:
    #     kategory = get_object_or_404(Kategory, slug=kategory_slug)
    #     devpost = devpost.filter(kategory=kategory)
    form = NewsLetterForm()
    return render(request, 'blog/post/devdetail.html', {'devpost': devpost,"letterForm":form,'categories': categories,'kategories': kategories,'common_tags':common_tags, })


def search_results(request, category_slug=None):
    categories = Category.objects.all()
    kategories = Kategory.objects.all()
    post = Post.objects.filter(status='published')
    devpost = DevPost.objects.filter(status='published')
    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if category_slug:
        posts = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'blog/post/search.html',{"message":message,"articles": searched_articles, 'categories': categories, 'post': post,'kategories': kategories,})   
    else:
        message = "You haven't searched for any term"

        return render(request, 'blog/post/search.html',{"message":message, 'categories': categories, 'post': post ,'kategories': kategories,})



def devsearch_results(request, category_slug=None):
    categories = Category.objects.all()
    kategories = Kategory.objects.all()
    post = Post.objects.filter(status='published')
    devpost = DevPost.objects.filter(status='published')
    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if category_slug:
        posts = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = DevPost.devsearch_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'blog/post/devsearch.html',{"message":message,"articles": searched_articles, 'categories': categories, 'post': post,'kategories': kategories,'devpost':devpost,})   
    else:
        message = "You haven't searched for any term"

        return render(request, 'blog/post/devsearch.html',{"message":message, 'categories': categories, 'post': post ,'kategories': kategories,'devpost':devpost})



def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)