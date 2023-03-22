# users/views.py
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from users.serializers import UserSerializer


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
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
    if request.user.is_authenticated:
        response = ("<h1>Bienvenue ! Vous êtes connecté avec {email}</h1> \n"
                    "        <ul>\n"
                    "            <h2><li>Veuillez créer un utilisateur en cliquant sur le lien suivant :\n"
                    "                <a href=http://127.0.0.1:8000/api-auth/users/create/>http://127.0.0.1:8000/"
                    "api-auth/users/create/</a>\n"
                    "            </li></h2>\n"
                    "            <h2><li>Veuillez se déconnecter en cliquant sur le lien suivant :\n"
                    "                <a href=http://127.0.0.1:8000/api-auth/logout/>http://127.0.0.1:8000/"
                    "api-auth/logout/</a>\n"
                    "            </li></h2>\n"
                    "        </ul>")
        return HttpResponse(response.format(email=request.user.email))

    response = ("<h1>Veuillez se connecter via Django REST framework en cliquant sur le lien suivant :</h1>\n"
                "    <h2><li>\n"
                "        <a href=http://127.0.0.1:8000/api-auth/login/>http://127.0.0.1:8000/api-auth/login/</a>\n"
                "    </li></h2>")
    return HttpResponse(response)
