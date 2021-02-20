from app.models import Post, Category


def categories(request):
    categories = Category.objects.all()
    cat_dict = {'categories': categories}
    return cat_dict


def user_liked_posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(likes=request.user.id)
        return {'user_liked_posts': posts}

    return {'user_liked_posts': None}


def recent_posts(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return {'recent_posts': posts}
