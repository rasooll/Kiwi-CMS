from blog.models import Blog, Category
from tagging.models import Tag, TaggedItem
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug),
        'tags': Blog.objects.filter(slug=slug)[0].tags.split(',')
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def view_tags(request, name):
    tagid = Tag.objects.filter(name=name)[0].id
    posts_tag = TaggedItem.objects.filter(tag_id=tagid)
    posts = []
    for post in posts_tag:
        object2 = Blog.objects.filter(id=post.object_id)
        posts.append(object2[0])
    return render_to_response('view_tag.html', {
        'posts': posts,
        'tag': name
    })