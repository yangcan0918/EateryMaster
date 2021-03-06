from django.conf.urls import patterns, include, url
from CookeryMaster import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EateryMaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^djangoadmin/', include(admin.site.urls)),

    url(r'^login/$', views.login),
    url(r'^logout/$',views.logout),
    url(r'^$',views.index),
    url(r'^signup/$', views.signup),
    url(r'^userpanel/overview/$',views.overview),

    url(r'^about/$',views.about),
    url(r'^guestbook/$',views.guestbook),
    url(r'^guestbook/reply/$',views.reply),
    url(r'^addrestaurant/$',views.addrestaurant),
    url(r'^addwindow/$',views.addwindow),
    url(r'^adddish/$',views.adddish),
    url(r'^canteens/$',views.canteens),
    url(r'^windows/$',views.windows),
    url(r'^dishes/$',views.dishes),
    url(r'^disheslist/$',views.disheslist),
    url(r'^windowslist/$',views.windowlist),
    url(r'^restaurantlist/$',views.restaurantlist),
    url(r'^allassessment/$',views.allassessment),
    url(r'^news/addanno/$', views.addanno),
    url(r'^news/index/$',views.newsindex),
    url(r'^news/add/$', views.addnews),
    url(r'^news/detail/$', views.newsdetail),
    url(r'^recommend/$', views.recommend),
    url(r'^image/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIAS_PATH}),
)
