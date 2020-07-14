from django.shortcuts import render
from .models import Post


# posts = [
#     {   'author' : 'Joseph Sowah',
#         'title' : 'The baker and the beauty',
#         'content' : 'Its a nice story about how a baker fell in love',
#         'date_posted' : 'April 12, 2020'
#     },

#     {
#         'author' : 'Blessing Adarkwa',
#         'title' : 'God is all powerful',
#         'content' : 'The nature and power of God',
#         'date_posted' : 'August 15, 2020'
        
#     }
# ]


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})