from django.urls import URLPattern, path, include
from django.views.generic import RedirectView
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

from . import views
# from . import models

# router = routers.DefaultRouter()
# router.register(r'helloworld', views.HelloWorldView, basename='HelloWorldMod')

urlpatterns: list[URLPattern] = [
    # path('', include(router.urls)),
    # path(
    #     route="",
    #     view=RedirectView.as_view(permanent=False, url="/api/public"),
    #     name="index",
    # ),
    # path(route="api/private-scoped", view=views.privateScoped, name="private_scoped"),
    path(route='helloworld/', view=views.HelloWorldView.as_view(), name="change-avatar"),
    path('admin/', admin.site.urls)
]
