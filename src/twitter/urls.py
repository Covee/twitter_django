from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from hashtags.views import HashTagView
from tweets.api.views import SearchTweetAPIView
from tweets.views import TweetListView
from .views import home, SearchView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', TweetListView.as_view(), name='home'),
	url(r'^search/$', SearchView.as_view(), name='search'),

	url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
	url(r'^tweet/', include('tweets.urls', namespace='tweet')),

	url(r'^api/search/$', SearchTweetAPIView.as_view(), name='search-api'),
	url(r'^api/tweet/', include('tweets.api.urls', namespace='tweet-api')),
	url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),

	url(r'^', include('accounts.urls', namespace='profiles')),
]


if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))