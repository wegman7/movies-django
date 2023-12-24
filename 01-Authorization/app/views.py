from django.http import HttpRequest, JsonResponse
from .authorization import RequestToken, authorized, can, getRequestToken
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from .permissions import ReadMessagesPermission


def public(request: HttpRequest()) -> JsonResponse:
    token: RequestToken | None = getRequestToken(request)
    print(token)

    return JsonResponse(
        data={
            "message": "Hello from a public endpoint! You don't need to be authenticated to see this.",
            "token": token.dict(),
        }
    )


@authorized
def private(request: HttpRequest, token: RequestToken) -> JsonResponse:
    return JsonResponse(
        data={
            "message": "Hello from a private endpoint! You need to be authenticated to see this.",
            "token": token.dict(),
        }
    )


@can("read:messages")
def privateScoped(request: HttpRequest, token: RequestToken) -> JsonResponse:
    return JsonResponse(
        data={
            "message": "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.",
            "token": token.dict(),
        }
    )


class HelloWorldView(generics.GenericAPIView):

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAuthenticated, ReadMessagesPermission)
    # permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        return Response(status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response

@authorized
@api_view(['GET'])
def hello_world(request: HttpRequest, token: RequestToken):
    print(token.dict())
    return Response({"message": "Hello, world!"})