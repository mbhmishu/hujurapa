from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required 
from blogapp.models import  Follow,Blog,Comment,Likes ,User
from blogapp.forms import CommentForm
from django.views.generic import UpdateView, DeleteView, CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid


# Create your views here.

class CratBlogView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog/add_blog.html'
    fields = ('title','blog_content','blog_img',)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        title = obj.title
        obj.slug = title.replace("","-") + "-" + str(uuid.uuid4())
        obj.save()
        return HttpResponseRedirect(reverse('blog_app:my_blog'))




@login_required
def blog_detail(request,slug):
    following_list = Follow.objects.filter(follower=request.user)
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    alrady_like = Likes.objects.filter(blog=blog, user=request.user)
    if alrady_like:
        likes = True
    else:
        likes = False
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_app:blog_detail' , kwargs={'slug':slug}))
            
    return render(request, 'blog/blog_details.html', context={'blog':blog, 'form':comment_form, 'likes':likes,'following_list':following_list})
    
    
@login_required
def Liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    alrady_like = Likes.objects.filter(blog=blog, user=user)
    if not alrady_like:
        likepost = Likes(blog=blog, user=user)
        likepost.save()
    return HttpResponseRedirect(reverse('blog_app:blog_detail', kwargs={'slug':blog.slug}))

@login_required
def Unlike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    alrady_like = Likes.objects.filter(blog=blog, user=user)
    alrady_like.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_detail', kwargs={'slug':blog.slug}))


class my_blog(LoginRequiredMixin,TemplateView):
    template_name= 'blog/my_blog.html'

class UdateBlogs(LoginRequiredMixin, UpdateView):
    model= Blog
    fields=('title','blog_content','blog_img')
    template_name= 'blog/add_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_app:my_blog' )




class DeleteBlogs(LoginRequiredMixin, DeleteView):
    context_object_name ='blog'
    model = Blog
    success_url = reverse_lazy('blog_app:my_blog')
    template_name = 'blog/delete_blog.html'




@login_required
def blog_list(request):
    following_list = Follow.objects.filter(follower=request.user)
    blog = Blog.objects.order_by('creat_date')
    posts = Blog.objects.filter(author__in=following_list.values_list('following'))
    post_like= Likes.objects.filter(user=request.user)
    post_like_list = post_like.values_list('blog', flat=True)
    
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)

    return render(request, 'blog/blog_list.html', context={'results': results, 'Search': Search,'posts': posts, 'post_like_list':post_like_list, 'blog':blog})




@login_required
def follow(request, username):
    to_follow = User.objects.get(username=username)
    from_follow = request.user
    alrady_follow = Follow.objects.filter(follower=from_follow,following=to_follow)
    if not alrady_follow:
        followed = Follow(follower=from_follow,following=to_follow)
        followed.save()
        return HttpResponseRedirect(reverse('blog_app:blog_list'))

        
@login_required
def unfollow(request, username):
    to_follow = User.objects.get(username=username)
    from_follow = request.user
    alrady_follow = Follow.objects.filter(follower=from_follow,following=to_follow)
    alrady_follow.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_list'))




