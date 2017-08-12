from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponse,HttpResponseRedirect
from .models import User, Tag,Article
from .forms import UserForm, ArticleForm,UserRegister,UserUpdateForm

# Create your views here.
#初始界面的登陆和注册按键
#首页需改进，页面太花
#点击我的主页时跳转原界面
#个人设置不对


def firstpage(req):
    return render(req,'zhihu/firstpage.html')


def article_list(req,id):
    user=User.objects.get(id=id)
    articles = Article.objects.order_by('-publish_time')
    return render(req, 'zhihu/playground.html', {'articles':articles, 'user':user})


def article_detail(request,id):
    article = Article.objects.get(id=id)
    return render(request,'zhihu/playground.html', {'article': article})


def article_add(req,id):
    if req.method == "POST":
        article = ArticleForm(req.POST)
        if article.is_valid():
            title=article.cleaned_data['title']
            tags = article.cleaned_data['tags']
            context = article.cleaned_data['context']
            context = context.replace("<p>", "")
            context = context.replace("</p>", "")
            for tag in tags.split():
                Tag.objects.get_or_create(tag_name=tag.strip())
            author=User.objects.get(id=id)
            article_new = Article.objects.create(title=title,context=context,author=author)
            article_new.save()
            for tag in tags.split():
                article_new.tags.add(Tag.objects.get(tag_name=tag.strip()))
                article_new.save()
            return redirect('article_list', id=author.id)
    else:
        article = ArticleForm()
    return render_to_response( 'zhihu/editor.html')


def article_update(request,id):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.author
            post.save()
            return redirect('article_list', id=post.pk)
    else:
        form = ArticleForm()
    return render(request, 'zhihu/article_update.html', {'form': form})


def author_update(request,id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            sex = form.cleaned_data['sex']
            sch = form.cleaned_data['sch']
            major = form.cleaned_data['major']
            grade = form.cleaned_data['grade']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            User.objects.filter(id=id).update(profile=request.FILES['profile'], username=username,sex=sex,major=major,grade=grade,email=email,phone_number=phone_number,sch=sch)
            return redirect('author_update',id=user.id)
    return render(request, 'zhihu/selfsetting.html', {'user': user})


def author_detail(request,id):
    author = get_object_or_404(User,pk=id)
    return render(request,'zhihu/author_detail.html',{'author':author})


def login(req):
    if req.method == "POST":
        user = UserForm(req.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user_return = User.objects.get(username=username)
            user_test = User.objects.filter(username__exact=username, password__exact=password)

            if user_test:
                return redirect('article_list',id=user_return.id)
            else:
                return render_to_response('registration/login.html')
    else:
        user = UserForm()
    return render_to_response('registration/login.html',)


def register(req):
    if req.method == "POST":
        user = UserRegister(req.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password1 = user.cleaned_data['password1']
            password2 = user.cleaned_data['password2']
            email=user.cleaned_data['email']
            if password1==password2:
                user_test=User.objects.filter(username__exact=username)
                if user_test:
                    return render_to_response('registration/login.html')
                else:
                    user_create=User.objects.create(username=username,password=password1,email=email)
                    user_create.save()
                    return redirect('login')
            else:
                return render_to_response('registration/register.html')
        else:
            return render_to_response('registration/register.html')
    else:
        user=UserRegister()
    return render_to_response('registration/register.html',)


def mypage(req, id):
    user = User.objects.get(id=id)
    articles = Article.objects.filter(author=user).order_by('-publish_time')
    return render(req, 'zhihu/playground.html', {'articles':articles, 'user':user})






