from blog.models import Post, Category, Comment, Page
from tagging.models import Tag, TaggedItem
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    """
    This view use for index page of the site
    """

    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request, slug):
    """
    This is use for single post page view
    """
    post = Post.objects.filter(slug=slug)[0]
    tags = post.tags
    if tags:
        # Remove space before and after of tag
        newTags = tags.replace(' ,', ',').replace(', ', ',').split(',')
    else:
        newTags = False
    comments = Comment.objects.filter(post=post)
    if not comments:
        comments = False

    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'tags': newTags,
        'comments': comments
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

    tagid = get_object_or_404(Tag, name=name)
    posts_tag = TaggedItem.objects.filter(tag_id=tagid)
    posts = []
    for post in posts_tag:
        object2 = Post.objects.filter(id=post.object_id)
        posts.append(object2[0])
    return render_to_response('view_tag.html', {
        'posts': posts,
        'tag': name
    })

def view_page(request, slug):
    """
    This is use for other page view
    """
    return render_to_response('view_page.html', {
        'page': get_object_or_404(Page, slug=slug),
    })