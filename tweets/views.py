from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from .forms import TweetForm, UserRegistarionForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')


def tweet_list(request):
   query = request.GET.get('q')
   tweets = Tweet.objects.all().order_by('-created_at')
   if query:
       tweets = tweets.filter(text__icontains=query)
   return render(request, 'tweet_list.html', {'tweets': tweets, 'query': query})


@login_required
def tweet_create(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            messages.success(request, 'Tweet created successfully!')
            return redirect('tweet_list') 
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
    else:
       form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user=request.user)
    if request.method=='POST':
       form=TweetForm(request.POST,request.FILES,instance=tweet)
       if form.is_valid():
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           messages.success(request, 'Tweet updated successfully!')
           return redirect('tweet_list')
       else:
           messages.error(request, 'Something went wrong. Please check the form.')
    else: 
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

@login_required 
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id,user=request.user)
    if request.method =='POST':
        tweet.delete()
        messages.success(request, 'Tweet deleted successfully!')
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method =='POST':
      form= UserRegistarionForm(request.POST)      
      if form.is_valid():
          user=form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request, user)
          messages.success(request, f'Welcome {user.username}! Your account has been created.')
          return redirect('tweet_list')
      else:
          messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
         form=UserRegistarionForm()
     
    return render(request,'registration/register.html',{'form':form})



def about_view(request):
    return render(request, 'about.html')
 
 
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
 
