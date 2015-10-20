from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article
from article.models import Comments
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from article.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth

# Create your views here.

def basic_one(request):
    view = "basic one"
    html = "<html><body>This is %s view</html></body>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three"
    return render_to_response("myview.html", {'name': view})


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    return render_to_response("articles.html", {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})


def article(request, article_id=1, comment_number=1):
    comment_form = CommentForm
    all_comment = Comments.objects.filter(comments_article_id=article_id)
    current_comment = Paginator(all_comment, 2)
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = current_comment.page(comment_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, articles_number, article_id):
    #redirect('')
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('http://127.0.0.1:8000/page/%s/' % articles_number)
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('http://127.0.0.1:8000/page/%s/' % articles_number)


def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('http://127.0.0.1:8000/articles/get/%s/' % article_id)