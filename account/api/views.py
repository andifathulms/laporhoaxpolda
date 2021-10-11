from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, UserSerializer, TokenSerializer

from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from account.models import Account

# Register API
class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer

class UserDetailGeneral(generics.ListAPIView):
    queryset = Account.objects.all().filter(is_staff=True)
    serializer_class = UserSerializer

class TokenUserList(generics.RetrieveAPIView):
    queryset = AuthToken.objects.all()
    serializer_class = TokenSerializer

@csrf_exempt
def getUser(request):
    data = request.headers
    try:
        user = [Account.objects.get(email=data["email"])]
    except Account.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        #print(serializer)
        return JsonResponse(serializer.data, safe=False)

