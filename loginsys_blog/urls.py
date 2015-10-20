from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/', 'loginsys_blog.views.login'),
    url(r'^logout/', 'loginsys_blog.views.logout'),
    url(r'^register/', 'loginsys_blog.views.register'),
]
