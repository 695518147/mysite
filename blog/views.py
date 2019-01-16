from django.shortcuts import redirect, render
from datetime import datetime
from blog.models import BlogPost, BlogPostForm
from django.http import HttpResponse


# Create your views here.
def archive(request):
    userId = request.GET.get('userId')
    posts = BlogPost.objects.filter(userId=userId)
    # template = loader.get_template("archive.html")
    # HttpResponse(template.render({'posts': posts}))
    return render(request, "archive.html", {'posts': posts, 'form': BlogPostForm()})


def create_blogpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return redirect('/blog?userId=' + str(post.userId))


def index(request):
    # 业务逻辑代码
    return HttpResponse("服务启动成功！")
