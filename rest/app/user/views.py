from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest.app.user.serializers import UserRegistrationSerializer
from rest.app.user.serializers import UserLoginSerializer
import pdb

class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        # pdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        # pdb.set_trace()
        serializer.is_valid(raise_exception=True)

        # id: user.id,
        # username: user.username,
        # firstName: user.firstName,
        # lastName: user.lastName,
        # token: 'fake-jwt-token'
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'user' : {
                    'id': serializer.data['id'],
                    'username': serializer.data['username'],
                    'first_name': serializer.data['first_name'],
                    'last_name': serializer.data['last_name'],
                    'token' : serializer.data['token'],
                }
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)