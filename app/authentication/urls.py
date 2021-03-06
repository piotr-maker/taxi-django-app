from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
	path('users/<int:pk>/', views.CustomUserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
