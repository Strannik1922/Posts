import json
from django.shortcuts import render

from .forms import CreatePost
from .models import Posts

posts = []


def index(request):
    error = ''
    post_data = ''

    all_posts = Posts.objects.all()
    form = CreatePost(data=request.POST)

    if request.method == "POST":
        posts.append(request.body.decode('utf-8'))
        if len(posts) >= 2 and '{"count":' in posts[-2]:

            posts[:] = posts[-2:]
            posts[0] = json.loads(posts[0])

            if form.is_valid():
                post = form.save(commit=False)
                post.count = posts[0].get('count')
                post.save()

                form = CreatePost()
                post_data = f'ID записи: {post.id} | Дата создания: {post.created_at}'
            else:
                error = 'Форма была неверной'

    data = {'form': form, 'error': error, 'data': post_data, 'posts': all_posts}

    return render(request, 'main/index.html', data)
