from blog.models import Post, Category, Comment, Page, GeneralSetting, Navbar
from tagging.models import Tag, TaggedItem
from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth import login, logout, authenticate
from .forms import SendComment, SignUpForm, UserLogin
from . import utils

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
    return render(
        request,
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
        if submitForm.is_valid() and utils.reCAPTCHA_is_valid(request) :
            formSuccess = True
            formData = submitForm.save(commit=False)
            formData.post = post
            formData.accepted = False
            formData.save()
        else:
            err = submitForm.errors
            if not utils.reCAPTCHA_is_valid(request):
                err['captcha'] = '''
                    <ul class="errorlist">
                        <li>
                            تشخیص مقابله با ربات صورت نگرفت.
                        </li>
                    </ul>
                '''
            formValue = submitForm.cleaned_data
    else:
        submitForm = SendComment()

    return render(request, 'view_post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'tags': newTags,
        'comments': comments,
        'form': submitForm,
        'formSuccess': formSuccess,
        'err': err,
        'formValue': formValue,
        'recaptcha': utils.reCAPTCHA_Script()
    })

def view_category(request, slug):
    """
    This is use for view all post of one category.
    """
    category = get_object_or_404(Category, slug=slug)
    return render(
        request,
        'view_category.html', {
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
    return render(
        request,
        'view_tag.html', {
        'posts': posts,
        'tag': name,
        'count': count
    })

def view_page(request, slug):
    """
    This is use for other page view
    """
    return render(
        request,
        'view_page.html', {
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
    return render(
        request,
        'index.html',
        {
            'page': Page,
            'has_previous': HasPrevious,
            'has_next': HasNext,
            'previous_number': PreviousNumber,
            'next_number': NextNumber
        }
    )

def user_registration(request):
    """
    This view user for user registration.
    """

    if request.user.is_authenticated:
        return redirect('index')
    err = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and utils.reCAPTCHA_is_valid(request):
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'user_registeration_done.html')

        else:
            err = form.errors
            if not utils.reCAPTCHA_is_valid(request):
                err['captcha'] = '''
                    <ul class="errorlist">
                        <li>
                            تشخیص مقابله با ربات صورت نگرفت.
                        </li>
                    </ul>
                '''
    else:
        form = SignUpForm()
    return render(request, 'user_register.html', {
        'form': form,
        'err': err,
        'recaptcha': utils.reCAPTCHA_Script()
        })

def user_login(request):
    """
    This view use for login page.
    """
    err = {}
    user = None
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid() and utils.reCAPTCHA_is_valid(request):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
        else:
            if not utils.reCAPTCHA_is_valid(request):
                err['captcha'] = '''
                    <ul class="errorlist">
                        <li>
                            تشخیص مقابله با ربات صورت نگرفت.
                        </li>
                    </ul>
                '''
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            err['auth'] = 'نام کاربری یا کلمه عبور صحیح نیست'
    else:
        form = UserLogin()
    return render(request, 'user_login.html', {
        'form': form,
        'err': err,
        'recaptcha': utils.reCAPTCHA_Script()
    })

def user_logout(request):
    """
    This view use for logout.
    """
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('index')