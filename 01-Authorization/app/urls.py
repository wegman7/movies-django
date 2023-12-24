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
    path(route="api/public", view=views.public, name="public"),
    path(route="api/private", view=views.private, name="private"),
    path(route="api/private-scoped", view=views.privateScoped, name="private_scoped"),
    path(route='helloworld/', view=views.HelloWorldView.as_view(), name="change-avatar"),
    path(route="api/hello-world", view=views.hello_world, name="hello-world"),
    path('admin/', admin.site.urls)
]
