from django.contrib.sessions.backends import file
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    odering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)


    def test_func(self):
        """Test to see if the user updating the post is the one who created it"""
        post = self.get_object()
        if self.request.user ==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post   
    success_url = '/'
    def test_func(self):
        """Test to see if the user updating the post is the one who created it"""
        post = self.get_object()
        if self.request.user ==post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})