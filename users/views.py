from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner


class UserView(APIView):
    def post(self, request: Request) -> Response:
        """
        Registro de usuários
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def get(self, request: Request, pk: int) -> Response:
        """
        Obtençao de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request, pk: int) -> Response:
        """
        Atualização de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        """
        Deleçao de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
