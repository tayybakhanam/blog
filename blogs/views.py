from django.shortcuts import render
from .models import Blog

# Create your views here.
def homeView(request):
    blog_list = Blog.objects.all()
   
    # for post in post_list:
    #     print(post.body)
    

    return render(request, 'index.html', {
        'blog': blog_list,
        'test': 'this is the testing message'
    })

# Create your views here.
