from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:id>/', views.OrderDetail.as_view()),
]
