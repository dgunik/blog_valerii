from django.conf.urls import include, url


urlpatterns = [
    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_three_simple'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/(?P<comment_number>\d+)/$', 'article.views.article'),
    url(r'^articles/addlike/(?P<articles_number>\d+)/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^page/(\d+)/$', 'article.views.articles'),
    url(r'^', 'article.views.articles'),
]

