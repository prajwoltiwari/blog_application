from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Prajwol Tiwari',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '5 Feb, 2019'
    },
    {
        'author': 'Prajwol Tiwari',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '6 Feb, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
