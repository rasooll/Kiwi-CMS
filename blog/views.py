from blog.models import Post, Category, Comment, Page, GeneralSetting, Navbar
from tagging.models import Tag, TaggedItem
from django.shortcuts import render_to_response, get_object_or_404, redirect,render
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from .forms import SendComment
from django.http import Http404

def get_post_pagination(number):
    """
    This function use for get post for pagination.
    """
    try:
        PNumber = GeneralSetting.objects.all()[0].PostNumber
    except IndexError:
        PNumber = 10
    AllPage = Post.objects.all()
    Pages = Paginator(AllPage, PNumber)
    Page = Pages.get_page(number)
    return Page


def index(request):
    """
    This view use for index page of the site
    """
    Page = get_post_pagination(1)
    HasNext = Page.has_next()
    if HasNext:
        NextNumber = Page.next_page_number()
    else:
        NextNumber = None
    return render_to_response(
        'index.html',
        {
            'page': Page,
            'has_next': HasNext,
            'has_previous': False,
            'next_number': NextNumber
        })

def view_post(request, slug):
    """
    This is use for single post page view
    """
    try:
        post = Post.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404
    tags = post.tags
    if tags:
        # Remove space before and after of tag
        newTags = tags.replace(' ,', ',').replace(', ', ',').split(',')
    else:
        newTags = False
    comments = Comment.objects.filter(post=post, accepted=True)
    if not comments:
        comments = False
    formSuccess = False
    err = {}
    formValue = {}
    if request.method == 'POST':
        submitForm = SendComment(request.POST)
        if submitForm.is_valid():
            formSuccess = True
            formData = submitForm.save(commit=False)
            formData.post = post
            formData.accepted = False
            formData.save()
        else:
            err = submitForm.errors
            formValue = submitForm.cleaned_data
            

    return render(request, 'view_post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'tags': newTags,
        'comments': comments,
        'formSuccess': formSuccess,
        'err': err,
        'formValue': formValue
    })

def view_category(request, slug):
    """
    This is use for view all post of one category.
    """
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })

def view_tags(request, name):
    """
    This is use for view all post when this tag include on this posts. 
    """
    try:
        tagid = Tag.objects.get(name=name)
    except ObjectDoesNotExist:
        tagid = False
    if tagid:
        posts = TaggedItem.objects.filter(tag_id=tagid)
        count = posts.count()
    else:
        posts = False
        count = 0
    return render_to_response('view_tag.html', {
        'posts': posts,
        'tag': name,
        'count': count
    })

def view_page(request, slug):
    """
    This is use for other page view
    """
    return render_to_response('view_page.html', {
        'page': get_object_or_404(Page, slug=slug)
    })

def Pagination(request, number):
    """
    This is for pagination page
    """
    Page = get_post_pagination(number)
    if (Page.number < number) or (Page.number == 1):
        return redirect('index')
    HasPrevious = Page.has_previous()
    if HasPrevious:
        PreviousNumber = Page.previous_page_number()
    else:
        PreviousNumber = None
    HasNext = Page.has_next()
    if HasNext:
        NextNumber = Page.next_page_number()
    else:
        NextNumber = None
    return render_to_response(
        'index.html',
        {
            'page': Page,
            'has_previous': HasPrevious,
            'has_next': HasNext,
            'previous_number': PreviousNumber,
            'next_number': NextNumber
        }
    )