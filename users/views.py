# users/views.py
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from users.models import CustomUser
from users.serializers import UserSerializer


class CreateUser(CreateAPIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user_data = {
                'user': UserSerializer(user).data,
                'message': "User has been created successfully."
            }
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    response = ("<h1>Please signup or login or logout via our API :</h1>\n"
                " <h2><li>\n"
                " <a href=http://127.0.0.1:8000/signup/>http://127.0.0.1:8000/signup/</a>\n"
                " </li></h2>"
                " <h2><li>\n"
                " <a href=http://127.0.0.1:8000/login/>http://127.0.0.1:8000/login/</a>\n"
                " </li></h2>"
                " <h2><li>\n"
                " <a href=http://127.0.0.1:8000/logout/>http://127.0.0.1:8000/logout/</a>\n"
                " </li></h2>")
    return HttpResponse(response)
