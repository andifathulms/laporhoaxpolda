from django.urls import path

from .views import FeedList, FeedDetail, FeedAPIList, FeedAPIDetail

urlpatterns = [
	path('feeds/', FeedAPIList.as_view()),
	path('feeds/<int:pk>/', FeedAPIDetail.as_view()),
]