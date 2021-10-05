from django.urls import path

from .views import ReportList, ReportDetail, ReportbyUser, ReportAPIList, ReportAPIDetail, CategoryAPIList
urlpatterns = [
	path('reports/', ReportAPIList.as_view()),
	path('reports/cat/', CategoryAPIList.as_view()),
	path('reports/<int:pk>/', ReportAPIDetail.as_view()),
	path('reports/user/<int:pk>/',ReportbyUser.as_view()),
]